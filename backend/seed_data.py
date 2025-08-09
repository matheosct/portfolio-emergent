from database import portfolio_collection, services_collection, projects_collection
from models import Portfolio, PersonalInfo, AboutInfo, Experience, NavigationItem, Service, Project
import asyncio

async def seed_database():
    """Seed database with initial portfolio data"""
    
    # Clear existing data
    await portfolio_collection.delete_many({})
    await services_collection.delete_many({})
    await projects_collection.delete_many({})
    
    # Seed portfolio data
    portfolio_data = Portfolio(
        personal=PersonalInfo(
            name="Alex Rivera",
            title="Visual Designer",
            tagline="Crafting meaningful digital experiences through thoughtful design",
            email="hello@alexrivera.design",
            phone="+1 (555) 123-4567",
            location="New York, NY"
        ),
        about=AboutInfo(
            bio="I'm a passionate visual designer with 6+ years of experience creating impactful digital and print designs. I believe great design should not only look beautiful but also solve real problems and connect with people on an emotional level.",
            experience=[
                Experience(role="Senior Visual Designer", company="Creative Studio NYC", period="2022 - Present"),
                Experience(role="Digital Designer", company="Brand Agency Co.", period="2020 - 2022"),
                Experience(role="Junior Designer", company="Design Collective", period="2018 - 2020")
            ],
            skills=[
                "Adobe Creative Suite", "Figma", "Sketch", "InVision", "Principle",
                "After Effects", "Typography", "Color Theory", "User Research", "Prototyping"
            ]
        ),
        navigation=[
            NavigationItem(name="Work", href="#work"),
            NavigationItem(name="Services", href="#services"),
            NavigationItem(name="About", href="#about"),
            NavigationItem(name="Contact", href="#contact")
        ]
    )
    
    await portfolio_collection.insert_one(portfolio_data.dict())
    
    # Seed services data
    services_data = [
        Service(
            title="Brand Identity",
            description="Complete brand identity design including logos, color palettes, typography, and brand guidelines.",
            color="mid-purple",
            order=1
        ),
        Service(
            title="Web Design",
            description="Modern, responsive website design focused on user experience and conversion optimization.",
            color="mid-blue",
            order=2
        ),
        Service(
            title="UI/UX Design",
            description="User interface and experience design for web and mobile applications.",
            color="light-yellow",
            order=3
        ),
        Service(
            title="Print Design",
            description="Professional print materials including brochures, business cards, and marketing collateral.",
            color="mid-orange",
            order=4
        )
    ]
    
    for service in services_data:
        await services_collection.insert_one(service.dict())
    
    # Seed projects data
    projects_data = [
        Project(
            title="Bloom Coffee Co.",
            description="Complete brand identity and packaging design for artisan coffee company",
            category=["Brand Identity", "Packaging"],
            bgColor="light-pink",
            year="2024",
            client="Bloom Coffee Co.",
            order=1
        ),
        Project(
            title="TechStart Dashboard",
            description="SaaS dashboard interface design with focus on data visualization",
            category=["UI/UX Design", "Web Design"],
            bgColor="mid-blue",
            year="2024",
            client="TechStart Inc.",
            order=2
        ),
        Project(
            title="Nature Magazine",
            description="Editorial design and layout for quarterly environmental magazine",
            category=["Print Design", "Editorial"],
            bgColor="light-yellow",
            year="2023",
            client="Nature Magazine",
            order=3
        ),
        Project(
            title="Wellness App",
            description="Mobile app design for meditation and wellness tracking",
            category=["UI/UX Design", "Mobile"],
            bgColor="mid-green",
            year="2023",
            client="Mindful App",
            order=4
        ),
        Project(
            title="Local Restaurant Chain",
            description="Brand redesign and menu design for growing restaurant chain",
            category=["Brand Identity", "Print Design"],
            bgColor="mid-orange",
            year="2023",
            client="Taste Local",
            order=5
        ),
        Project(
            title="Financial Platform",
            description="Complete UX overhaul for personal finance management platform",
            category=["UI/UX Design", "Web Design"],
            bgColor="grey",
            year="2024",
            client="FinanceTrack",
            order=6
        )
    ]
    
    for project in projects_data:
        await projects_collection.insert_one(project.dict())
    
    print("Database seeded successfully!")

if __name__ == "__main__":
    asyncio.run(seed_database())