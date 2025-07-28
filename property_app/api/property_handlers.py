"""
Property API handlers for listing management
"""

from marshmallow import ValidationError
from api.base_handler import BaseHandler
from services.listing_service import ListingService
from models.property import PropertySchema, PropertyListSchema

class PropertyListHandler(BaseHandler):
    """Handle property listing operations"""
    
    def initialize(self):
        super().initialize()
        self.listing_service = ListingService()
    
    async def get(self):
        """Get list of properties with filtering"""
        try:
            # Check if the request is for the public API endpoint
            if self.request.path == "/public-api/listings":
                # Public API: only return active listings, no user_id filter
                page_num = int(self.get_argument('page_num', 1))
                page_size = int(self.get_argument('page_size', 10))
                user_id = self.get_argument('user_id', None)
                result = await self.listing_service.get_properties(
                    page_num=page_num,
                    page_size=page_size,
                    is_active=True,
                    user_id=user_id
                )
            else:
                # Default: allow user_id filter
                page_num = int(self.get_argument('page_num', 1))
                page_size = int(self.get_argument('page_size', 10))
                user_id = self.get_argument('user_id', None)
                result = await self.listing_service.get_properties(
                    page_num=page_num,
                    page_size=page_size,
                    user_id=user_id,
                    is_active=False
                )

            self.write_success(
                "listings",
                result, 
                "Properties retrieved successfully",
                200
            )

        except ValidationError as e:
            self.write_validation_error(e.messages)
        except Exception as e:
            self.write_error_response(str(e), 400)
    
    async def post(self):
        """Create new property listing (application/x-www-form-urlencoded)"""
        try:
            # Ensure content type is form-urlencoded
            if self.request.headers.get("Content-Type", "").startswith("application/x-www-form-urlencoded"):
                user_id = self.get_body_argument('user_id', None)
                listing_type = self.get_body_argument('listing_type', None)
                price = self.get_body_argument('price', None)
            else:
                self.write_error_response("Content-Type must be application/x-www-form-urlencoded", 400)
                return

            # Validate required parameters
            if user_id is None or listing_type is None or price is None:
                self.write_error_response("Missing required parameters", 400)
                return

            try:
                user_id = int(user_id)
                price = int(price)
            except ValueError:
                self.write_error_response("user_id and price must be integers", 400)
                return

            data = {
                "user_id": user_id,
                "listing_type": listing_type,
                "price": price
            }

            # Validate input
            schema = PropertySchema()
            validated_data = schema.load(data)

            # Create property
            property_obj = await self.listing_service.create_property(validated_data)

            self.write_success(
                "listings",
                property_obj.to_dict(),
                "Property created successfully",
                201
            )

        except ValidationError as e:
            self.write_validation_error(e.messages)
        except Exception as e:
            self.write_error_response(str(e), 400)