from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

class PersonalInfo(BaseModel):
    name: str
    title: str
    tagline: Optional[str] = None
    email: str
    phone: Optional[str] = None
    location: Optional[str] = None

class Experience(BaseModel):
    role: str
    company: str
    period: str

class AboutInfo(BaseModel):
    bio: Optional[str] = None
    experience: Optional[List[Experience]] = []
    skills: Optional[List[str]] = []

class NavigationItem(BaseModel):
    name: str
    href: str

class Portfolio(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    personal: PersonalInfo
    about: Optional[AboutInfo] = None
    navigation: Optional[List[NavigationItem]] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class PortfolioUpdate(BaseModel):
    personal: Optional[PersonalInfo] = None
    about: Optional[AboutInfo] = None
    navigation: Optional[List[NavigationItem]] = None

class Service(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    color: Optional[str] = "mid-purple"
    order: Optional[int] = 0
    active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class ServiceCreate(BaseModel):
    title: str
    description: str
    color: Optional[str] = "mid-purple"
    order: Optional[int] = 0

class ServiceUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    color: Optional[str] = None
    order: Optional[int] = None
    active: Optional[bool] = None

class Project(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    category: List[str] = []
    bgColor: Optional[str] = "light-pink"
    year: Optional[str] = None
    client: Optional[str] = None
    order: Optional[int] = 0
    active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class ProjectCreate(BaseModel):
    title: str
    description: str
    category: Optional[List[str]] = []
    bgColor: Optional[str] = "light-pink"
    year: Optional[str] = None
    client: Optional[str] = None
    order: Optional[int] = 0

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[List[str]] = None
    bgColor: Optional[str] = None
    year: Optional[str] = None
    client: Optional[str] = None
    order: Optional[int] = None
    active: Optional[bool] = None