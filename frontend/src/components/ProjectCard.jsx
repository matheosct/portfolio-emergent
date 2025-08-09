import React from 'react';
import { useNavigate } from 'react-router-dom';

const ProjectCard = ({ project }) => {
  const navigate = useNavigate();

  const getBackgroundColor = (bgColor) => {
    const colorMap = {
      'light-pink': 'bg-pink-100 text-gray-900',
      'mid-blue': 'bg-blue-500 text-white',
      'light-yellow': 'bg-yellow-200 text-gray-900',
      'mid-green': 'bg-green-500 text-white',
      'mid-orange': 'bg-orange-400 text-white',
      'grey': 'bg-gray-200 text-gray-900',
      'mid-purple': 'bg-purple-500 text-white'
    };
    return colorMap[bgColor] || 'bg-gray-100 text-gray-900';
  };

  const handleClick = () => {
    navigate(`/project/${project.id}`);
  };

  return (
    <div 
      className={`group rounded-lg p-8 min-h-[320px] flex flex-col justify-between cursor-pointer transition-all duration-300 hover:-translate-y-1 hover:shadow-xl ${getBackgroundColor(project.bgColor)}`}
      onClick={handleClick}
    >
      <div>
        <h3 className="text-xl font-medium mb-3 group-hover:underline">
          {project.title}
        </h3>
        <p className="text-base opacity-70 mb-4 leading-relaxed">
          {project.description}
        </p>
      </div>
      
      <div className="mt-auto">
        <div className="flex flex-wrap gap-2 mb-4">
          {project.category && project.category.map((cat, index) => (
            <span 
              key={index}
              className="px-3 py-1 text-xs font-medium bg-black/10 rounded-full uppercase tracking-wide"
            >
              {cat}
            </span>
          ))}
        </div>
        
        <div className="flex justify-between items-center text-sm opacity-60">
          <span>{project.client}</span>
          <span>{project.year}</span>
        </div>
      </div>
    </div>
  );
};

export default ProjectCard;