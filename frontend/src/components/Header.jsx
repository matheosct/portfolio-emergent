import React from 'react';
import { portfolioData } from '../mock';

const Header = () => {
  const { personal, navigation } = portfolioData;

  const scrollToSection = (href) => {
    const element = document.querySelector(href);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-white/90 backdrop-blur-md border-b border-gray-100">
      <div className="container mx-auto px-6 py-4">
        <div className="flex items-center justify-between">
          {/* Logo/Name */}
          <div className="flex items-center">
            <h1 className="text-xl font-medium text-gray-900 tracking-tight">
              {personal.name}
            </h1>
            <span className="ml-2 text-sm text-gray-500 hidden sm:block">
              {personal.title}
            </span>
          </div>

          {/* Navigation */}
          <nav className="hidden md:flex items-center space-x-8">
            {navigation.map((item) => (
              <button
                key={item.name}
                onClick={() => scrollToSection(item.href)}
                className="text-gray-700 hover:text-gray-900 font-medium text-sm tracking-wide transition-colors duration-200 hover:underline"
              >
                {item.name}
              </button>
            ))}
          </nav>

          {/* Mobile menu button */}
          <button className="md:hidden p-2 text-gray-700 hover:text-gray-900">
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header;