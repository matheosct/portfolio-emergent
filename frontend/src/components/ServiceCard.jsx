import React from 'react';

const ServiceCard = ({ service }) => {
  return (
    <div className="bg-white rounded-lg p-8 border border-gray-100 hover:border-gray-200 transition-all duration-300 hover:shadow-lg">
      <div className="mb-6">
        <div className="w-12 h-12 bg-gray-900 rounded-lg flex items-center justify-center mb-4">
          <div className="w-6 h-6 bg-white rounded-sm"></div>
        </div>
        <h3 className="text-xl font-medium text-gray-900 mb-3">
          {service.title}
        </h3>
      </div>
      
      <p className="text-gray-600 leading-relaxed">
        {service.description}
      </p>
      
      <button className="mt-6 text-gray-900 font-medium text-sm hover:underline transition-colors duration-200">
        Learn more →
      </button>
    </div>
  );
};

export default ServiceCard;