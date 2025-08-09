import React from "react";
import "./App.css";
import Header from './components/Header';
import ProjectCard from './components/ProjectCard';
import ServiceCard from './components/ServiceCard';
import { portfolioData } from './mock';

const App = () => {
  const { personal, projects, services, about } = portfolioData;

  const handleContactClick = () => {
    window.location.href = `mailto:${personal.email}`;
  };

  return (
    <div className="min-h-screen bg-white">
      <Header />
      
      {/* Hero Section */}
      <section className="pt-24 pb-16 px-6">
        <div className="container mx-auto max-w-4xl text-center">
          <h1 className="text-5xl md:text-7xl font-light text-gray-900 mb-6 tracking-tight leading-tight">
            {personal.name}
          </h1>
          <h2 className="text-xl md:text-2xl text-gray-600 mb-8 font-light">
            {personal.title}
          </h2>
          <p className="text-lg text-gray-700 max-w-2xl mx-auto leading-relaxed">
            {personal.tagline}
          </p>
        </div>
      </section>

      {/* Work Section */}
      <section id="work" className="py-20 px-6 bg-gray-50">
        <div className="container mx-auto max-w-6xl">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-light text-gray-900 mb-4">
              Selected Work
            </h2>
            <p className="text-lg text-gray-600 max-w-2xl mx-auto">
              A collection of recent projects showcasing design solutions across various industries
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {projects.map((project) => (
              <ProjectCard key={project.id} project={project} />
            ))}
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section id="services" className="py-20 px-6">
        <div className="container mx-auto max-w-6xl">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-light text-gray-900 mb-4">
              Services
            </h2>
            <p className="text-lg text-gray-600 max-w-2xl mx-auto">
              Comprehensive design solutions tailored to your business needs
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {services.map((service) => (
              <ServiceCard key={service.id} service={service} />
            ))}
          </div>
        </div>
      </section>

      {/* About Section */}
      <section id="about" className="py-20 px-6 bg-gray-50">
        <div className="container mx-auto max-w-4xl">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-light text-gray-900 mb-4">
              About
            </h2>
          </div>
          
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16">
            <div>
              <p className="text-lg text-gray-700 leading-relaxed mb-8">
                {about.bio}
              </p>
              
              <div className="mb-8">
                <h3 className="text-xl font-medium text-gray-900 mb-4">Experience</h3>
                <div className="space-y-4">
                  {about.experience.map((exp, index) => (
                    <div key={index} className="border-l-2 border-gray-200 pl-4">
                      <h4 className="font-medium text-gray-900">{exp.role}</h4>
                      <p className="text-gray-600">{exp.company}</p>
                      <p className="text-sm text-gray-500">{exp.period}</p>
                    </div>
                  ))}
                </div>
              </div>
            </div>
            
            <div>
              <h3 className="text-xl font-medium text-gray-900 mb-6">Skills & Tools</h3>
              <div className="flex flex-wrap gap-2">
                {about.skills.map((skill, index) => (
                  <span 
                    key={index}
                    className="px-3 py-2 bg-white border border-gray-200 rounded-full text-sm text-gray-700 hover:border-gray-300 transition-colors duration-200"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="py-20 px-6">
        <div className="container mx-auto max-w-4xl text-center">
          <h2 className="text-4xl md:text-5xl font-light text-gray-900 mb-8">
            Let's Work Together
          </h2>
          <p className="text-lg text-gray-600 mb-12 max-w-2xl mx-auto">
            Ready to start your next project? I'd love to hear about your ideas and discuss how we can bring them to life.
          </p>
          
          <div className="space-y-4 mb-12">
            <p className="text-lg text-gray-700">
              <strong>Email:</strong> {personal.email}
            </p>
            <p className="text-lg text-gray-700">
              <strong>Phone:</strong> {personal.phone}
            </p>
            <p className="text-lg text-gray-700">
              <strong>Location:</strong> {personal.location}
            </p>
          </div>
          
          <button 
            onClick={handleContactClick}
            className="bg-gray-900 text-white px-8 py-4 rounded-full font-medium hover:bg-gray-800 transition-colors duration-200 text-lg"
          >
            Get In Touch
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-8 px-6 border-t border-gray-100">
        <div className="container mx-auto max-w-6xl">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <p className="text-gray-600 text-sm">
              © 2024 {personal.name}. All rights reserved.
            </p>
            <div className="flex space-x-6 mt-4 md:mt-0">
              <a href="#" className="text-gray-600 hover:text-gray-900 text-sm transition-colors duration-200">
                LinkedIn
              </a>
              <a href="#" className="text-gray-600 hover:text-gray-900 text-sm transition-colors duration-200">
                Dribbble
              </a>
              <a href="#" className="text-gray-600 hover:text-gray-900 text-sm transition-colors duration-200">
                Behance
              </a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default App;