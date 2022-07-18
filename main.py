from fastapi import FastAPI
from core.config import settings
from db.session import engine  
from db.base import Base  
app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

# def include_router(app):
# 	app.include_router(general_pages_router)


# def configure_static(app):
#     app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables(): 
	Base.metadata.create_all(bind=engine)

	
def start_application():
	app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)
	#include_router(app)
	# configure_static(app)
	create_tables()
	return app

app = start_application()