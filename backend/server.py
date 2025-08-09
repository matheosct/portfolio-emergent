from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
import os
import logging
from pathlib import Path
from typing import List

# Import our models and database
from models import (
    Portfolio, PortfolioUpdate, 
    Service, ServiceCreate, ServiceUpdate,
    Project, ProjectCreate, ProjectUpdate
)
from database import (
    portfolio_collection, services_collection, projects_collection,
    convert_object_id, convert_object_ids, close_db_client
)

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Create the main app without a prefix
app = FastAPI(title="Designer Portfolio API")

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Portfolio endpoints
@api_router.get("/portfolio")
async def get_portfolio():
    """Get portfolio information (personal + about + navigation)"""
    try:
        portfolio_data = await portfolio_collection.find_one()
        if not portfolio_data:
            raise HTTPException(status_code=404, detail="Portfolio not found")
        
        portfolio_data = convert_object_id(portfolio_data)
        return {"success": True, "data": portfolio_data}
    except Exception as e:
        logging.error(f"Error fetching portfolio: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@api_router.put("/portfolio")
async def update_portfolio(portfolio_update: PortfolioUpdate):
    """Update portfolio information"""
    try:
        update_data = {k: v for k, v in portfolio_update.dict().items() if v is not None}
        
        result = await portfolio_collection.update_one(
            {}, 
            {"$set": update_data}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Portfolio not found")
            
        updated_portfolio = await portfolio_collection.find_one()
        updated_portfolio = convert_object_id(updated_portfolio)
        
        return {"success": True, "data": updated_portfolio}
    except Exception as e:
        logging.error(f"Error updating portfolio: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Services endpoints
@api_router.get("/services")
async def get_services():
    """Get all active services ordered by order field"""
    try:
        services_cursor = services_collection.find({"active": True}).sort("order", 1)
        services = await services_cursor.to_list(100)
        services = convert_object_ids(services)
        
        return {"success": True, "data": services}
    except Exception as e:
        logging.error(f"Error fetching services: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@api_router.post("/services")
async def create_service(service_data: ServiceCreate):
    """Create new service"""
    try:
        service = Service(**service_data.dict())
        result = await services_collection.insert_one(service.dict())
        
        created_service = await services_collection.find_one({"_id": result.inserted_id})
        created_service = convert_object_id(created_service)
        
        return {"success": True, "data": created_service}
    except Exception as e:
        logging.error(f"Error creating service: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@api_router.put("/services/{service_id}")
async def update_service(service_id: str, service_update: ServiceUpdate):
    """Update service"""
    try:
        update_data = {k: v for k, v in service_update.dict().items() if v is not None}
        
        result = await services_collection.update_one(
            {"id": service_id},
            {"$set": update_data}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Service not found")
            
        updated_service = await services_collection.find_one({"id": service_id})
        updated_service = convert_object_id(updated_service)
        
        return {"success": True, "data": updated_service}
    except Exception as e:
        logging.error(f"Error updating service: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@api_router.delete("/services/{service_id}")
async def delete_service(service_id: str):
    """Delete service (soft delete by setting active=False)"""
    try:
        result = await services_collection.update_one(
            {"id": service_id},
            {"$set": {"active": False}}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Service not found")
            
        return {"success": True, "message": "Service deleted successfully"}
    except Exception as e:
        logging.error(f"Error deleting service: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Projects endpoints
@api_router.get("/projects")
async def get_projects():
    """Get all active projects ordered by order field (for home page)"""
    try:
        projects_cursor = projects_collection.find({"active": True}).sort("order", 1)
        projects = await projects_cursor.to_list(100)
        projects = convert_object_ids(projects)
        
        return {"success": True, "data": projects}
    except Exception as e:
        logging.error(f"Error fetching projects: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@api_router.get("/projects/{project_id}")
async def get_project_detail(project_id: str):
    """Get individual project details by ID"""
    try:
        project = await projects_collection.find_one({"id": project_id, "active": True})
        
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
            
        project = convert_object_id(project)
        return {"success": True, "data": project}
    except Exception as e:
        logging.error(f"Error fetching project detail: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@api_router.post("/projects")
async def create_project(project_data: ProjectCreate):
    """Create new project"""
    try:
        project = Project(**project_data.dict())
        result = await projects_collection.insert_one(project.dict())
        
        created_project = await projects_collection.find_one({"_id": result.inserted_id})
        created_project = convert_object_id(created_project)
        
        return {"success": True, "data": created_project}
    except Exception as e:
        logging.error(f"Error creating project: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@api_router.put("/projects/{project_id}")
async def update_project(project_id: str, project_update: ProjectUpdate):
    """Update project"""
    try:
        update_data = {k: v for k, v in project_update.dict().items() if v is not None}
        
        result = await projects_collection.update_one(
            {"id": project_id},
            {"$set": update_data}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Project not found")
            
        updated_project = await projects_collection.find_one({"id": project_id})
        updated_project = convert_object_id(updated_project)
        
        return {"success": True, "data": updated_project}
    except Exception as e:
        logging.error(f"Error updating project: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@api_router.delete("/projects/{project_id}")
async def delete_project(project_id: str):
    """Delete project (soft delete by setting active=False)"""
    try:
        result = await projects_collection.update_one(
            {"id": project_id},
            {"$set": {"active": False}}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Project not found")
            
        return {"success": True, "message": "Project deleted successfully"}
    except Exception as e:
        logging.error(f"Error deleting project: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_db_client()