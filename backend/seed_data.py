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
    
    # Seed projects data with images
    projects_data = [
        Project(
            title="Bloom Coffee Co.",
            description="Complete brand identity and packaging design for artisan coffee company",
            detailed_description="A comprehensive brand identity project for Bloom Coffee Co., an artisan coffee roaster committed to sustainable sourcing. The project included logo design, packaging system, brand guidelines, and marketing materials. The visual identity reflects the company's values of quality, sustainability, and craftsmanship through warm earth tones and organic typography.",
            category=["Brand Identity", "Packaging"],
            bgColor="light-pink",
            year="2024",
            client="Bloom Coffee Co.",
            thumbnail_image="https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=800&h=600&fit=crop",
            static_images=[
                "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800&h=600&fit=crop",
                "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=800&h=600&fit=crop"
            ],
            carousel_images=[
                "https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1610889556528-9a770e32642f?w=1200&h=800&fit=crop"
            ],
            order=1
        ),
        Project(
            title="TechStart Dashboard",
            description="SaaS dashboard interface design with focus on data visualization",
            detailed_description="A modern dashboard interface design for TechStart's analytics platform. The project focused on creating intuitive data visualizations, streamlined user workflows, and responsive design patterns. The interface helps users make data-driven decisions through clear information hierarchy and interactive elements.",
            category=["UI/UX Design", "Web Design"],
            bgColor="mid-blue",
            year="2024",
            client="TechStart Inc.",
            thumbnail_image="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=600&fit=crop",
            static_images=[
                "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&h=600&fit=crop",
                "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=800&h=600&fit=crop"
            ],
            carousel_images=[
                "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?w=1200&h=800&fit=crop"
            ],
            order=2
        ),
        Project(
            title="Nature Magazine",
            description="Editorial design and layout for quarterly environmental magazine",
            detailed_description="Editorial design project for Nature Magazine's quarterly publication focusing on environmental conservation. The design system includes typography hierarchy, grid systems, infographic templates, and sustainable printing considerations. The layouts balance beautiful photography with readable content structure.",
            category=["Print Design", "Editorial"],
            bgColor="light-yellow",
            year="2023",
            client="Nature Magazine",
            thumbnail_image="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&h=600&fit=crop",
            static_images=[
                "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800&h=600&fit=crop",
                "https://images.unsplash.com/photo-1586953208448-b95a79798f07?w=800&h=600&fit=crop"
            ],
            carousel_images=[
                "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1586953208448-b95a79798f07?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=1200&h=800&fit=crop"
            ],
            order=3
        ),
        Project(
            title="Wellness App",
            description="Mobile app design for meditation and wellness tracking",
            detailed_description="Mobile application design for a comprehensive wellness platform featuring meditation sessions, mood tracking, and progress analytics. The interface prioritizes calm, soothing aesthetics while maintaining intuitive navigation and accessibility standards for daily wellness practices.",
            category=["UI/UX Design", "Mobile"],
            bgColor="mid-green",
            year="2023",
            client="Mindful App",
            thumbnail_image="https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800&h=600&fit=crop",
            static_images=[
                "https://images.unsplash.com/photo-1517077304055-6e89abbf09b0?w=800&h=600&fit=crop",
                "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=600&fit=crop"
            ],
            carousel_images=[
                "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1517077304055-6e89abbf09b0?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=1200&h=800&fit=crop"
            ],
            order=4
        ),
        Project(
            title="Local Restaurant Chain",
            description="Brand redesign and menu design for growing restaurant chain",
            detailed_description="Complete brand refresh for Taste Local, a farm-to-table restaurant chain expanding across the region. The project included logo redesign, menu design, signage systems, and digital presence. The new identity celebrates local ingredients and community connections through warm, inviting visuals.",
            category=["Brand Identity", "Print Design"],
            bgColor="mid-orange",
            year="2023",
            client="Taste Local",
            thumbnail_image="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&h=600&fit=crop",
            static_images=[
                "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800&h=600&fit=crop",
                "https://images.unsplash.com/photo-1493770348161-369560ae357d?w=800&h=600&fit=crop"
            ],
            carousel_images=[
                "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1493770348161-369560ae357d?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&h=800&fit=crop"
            ],
            order=5
        ),
        Project(
            title="Financial Platform",
            description="Complete UX overhaul for personal finance management platform",
            detailed_description="User experience redesign for FinanceTrack's personal finance management platform. The project involved user research, information architecture restructuring, and interface design to simplify complex financial data. The new design helps users understand their financial health through clear visualizations and actionable insights.",
            category=["UI/UX Design", "Web Design"],
            bgColor="grey",
            year="2024",
            client="FinanceTrack",
            thumbnail_image="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&h=600&fit=crop",
            static_images=[
                "https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=800&h=600&fit=crop",
                "https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=800&h=600&fit=crop"
            ],
            carousel_images=[
                "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=1200&h=800&fit=crop",
                "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=1200&h=800&fit=crop"
            ],
            order=6
        )
    ]
    
    for project in projects_data:
        await projects_collection.insert_one(project.dict())
    
    print("Database seeded successfully with project images!")

if __name__ == "__main__":
    asyncio.run(seed_database())