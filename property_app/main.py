"""
Main application entry point
Property Trading Application dengan Tornado
"""

import tornado.ioloop
import tornado.web
import motor.motor_tornado
from config.settings import Settings
from api.routes import get_routes
from utils.database import DatabaseManager

class PropertyApp(tornado.web.Application):
    def __init__(self):
        # Get application routes
        routes = get_routes()
        
        # Application settings
        settings = {
            "debug": Settings.DEBUG,
            "cookie_secret": Settings.SECRET_KEY,
            "xsrf_cookies": False,  # Disable for API
            "default_handler_class": NotFoundHandler,
        }
        
        super().__init__(routes, **settings)
        
        # Initialize database connection
        self.db = DatabaseManager().get_database()
        
        print(f"🏠 Property Trading App initialized")
        print(f"📊 Debug mode: {Settings.DEBUG}")
        print(f"🗄️  Database: {Settings.MONGO_DB_NAME}")

class NotFoundHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_status(404)
        self.write({"error": "Endpoint not found"})
    
    def post(self):
        self.get()
    
    def put(self):
        self.get()
    
    def delete(self):
        self.get()

def make_app():
    return PropertyApp()

if __name__ == "__main__":
    app = make_app()
    app.listen(Settings.PORT)
    
    print(f"🚀 Server running on http://localhost:{Settings.PORT}")
    print("📖 API Documentation:")
    print(f"   - Listings: http://localhost:{Settings.PORT}/api/listings")
    print(f"   - Users: http://localhost:{Settings.PORT}/api/users")
    print(f"   - Health: http://localhost:{Settings.PORT}/api/health")
    
    tornado.ioloop.IOLoop.current().start()
