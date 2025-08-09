import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation, Pagination, Autoplay } from 'swiper/modules';
import { projectsAPI } from '../services/api';
import LoadingSpinner from './LoadingSpinner';
import Header from './Header';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

const ProjectDetail = ({ portfolioData }) => {
  const { projectId } = useParams();
  const navigate = useNavigate();
  const [project, setProject] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProjectDetail = async () => {
      try {
        setLoading(true);
        const response = await projectsAPI.getProjectDetail(projectId);
        if (response.success) {
          setProject(response.data);
        }
      } catch (error) {
        console.error('Error fetching project detail:', error);
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    if (projectId) {
      fetchProjectDetail();
    }
  }, [projectId]);

  if (loading) {
    return (
      <div className="min-h-screen bg-white">
        {portfolioData && (
          <Header personal={portfolioData.personal} navigation={portfolioData.navigation} />
        )}
        <div className="pt-24 flex items-center justify-center min-h-[60vh]">
          <div className="text-center">
            <LoadingSpinner size="large" />
            <p className="mt-4 text-gray-600">Loading project details...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error || !project) {
    return (
      <div className="min-h-screen bg-white">
        {portfolioData && (
          <Header personal={portfolioData.personal} navigation={portfolioData.navigation} />
        )}
        <div className="pt-24 flex items-center justify-center min-h-[60vh]">
          <div className="text-center">
            <p className="text-red-600 mb-4">Error loading project: {error || 'Project not found'}</p>
            <button 
              onClick={() => navigate('/')} 
              className="bg-gray-900 text-white px-6 py-3 rounded-lg hover:bg-gray-800 transition-colors"
            >
              Back to Portfolio
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-white">
      {portfolioData && (
        <Header personal={portfolioData.personal} navigation={portfolioData.navigation} />
      )}
      
      {/* Back button */}
      <div className="pt-20 px-6">
        <div className="container mx-auto max-w-6xl">
          <button 
            onClick={() => navigate('/')}
            className="mb-8 flex items-center text-gray-600 hover:text-gray-900 transition-colors duration-200"
          >
            <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
            Back to Portfolio
          </button>
        </div>
      </div>

      {/* Project Header */}
      <section className="px-6 pb-12">
        <div className="container mx-auto max-w-6xl">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
            <div>
              <h1 className="text-4xl md:text-6xl font-light text-gray-900 mb-6 leading-tight">
                {project.title}
              </h1>
              
              <div className="flex flex-wrap gap-2 mb-8">
                {project.category && project.category.map((cat, index) => (
                  <span 
                    key={index}
                    className="px-4 py-2 bg-gray-100 text-gray-800 rounded-full text-sm font-medium"
                  >
                    {cat}
                  </span>
                ))}
              </div>
            </div>
            
            <div className="space-y-6">
              <div>
                <p className="text-lg text-gray-700 leading-relaxed mb-6">
                  {project.detailed_description || project.description}
                </p>
              </div>
              
              <div className="grid grid-cols-2 gap-6 text-sm">
                {project.client && (
                  <div>
                    <h3 className="font-medium text-gray-900 mb-1">Client</h3>
                    <p className="text-gray-600">{project.client}</p>
                  </div>
                )}
                {project.year && (
                  <div>
                    <h3 className="font-medium text-gray-900 mb-1">Year</h3>
                    <p className="text-gray-600">{project.year}</p>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Image Carousel */}
      {project.carousel_images && project.carousel_images.length > 0 && (
        <section className="px-6 py-12 bg-gray-50">
          <div className="container mx-auto max-w-6xl">
            <h2 className="text-2xl font-light text-gray-900 mb-8 text-center">Project Gallery</h2>
            
            <Swiper
              modules={[Navigation, Pagination, Autoplay]}
              spaceBetween={30}
              slidesPerView={1}
              navigation
              pagination={{ clickable: true }}
              autoplay={{
                delay: 5000,
                disableOnInteraction: false,
              }}
              loop={true}
              className="rounded-lg overflow-hidden shadow-lg"
              style={{ height: '500px' }}
            >
              {project.carousel_images.map((image, index) => (
                <SwiperSlide key={index}>
                  <div className="relative w-full h-full">
                    <img 
                      src={image} 
                      alt={`${project.title} - Image ${index + 1}`}
                      className="w-full h-full object-cover"
                      onError={(e) => {
                        e.target.src = 'https://via.placeholder.com/1200x500?text=Image+Not+Available';
                      }}
                    />
                  </div>
                </SwiperSlide>
              ))}
            </Swiper>
          </div>
        </section>
      )}

      {/* Static Images */}
      {project.static_images && project.static_images.length > 0 && (
        <section className="px-6 py-12">
          <div className="container mx-auto max-w-6xl">
            <h2 className="text-2xl font-light text-gray-900 mb-8 text-center">Project Details</h2>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              {project.static_images.map((image, index) => (
                <div key={index} className="rounded-lg overflow-hidden shadow-lg">
                  <img 
                    src={image} 
                    alt={`${project.title} - Detail ${index + 1}`}
                    className="w-full h-64 md:h-80 object-cover hover:scale-105 transition-transform duration-300"
                    onError={(e) => {
                      e.target.src = 'https://via.placeholder.com/800x600?text=Image+Not+Available';
                    }}
                  />
                </div>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* CTA Section */}
      <section className="px-6 py-16 bg-gray-900 text-white">
        <div className="container mx-auto max-w-4xl text-center">
          <h2 className="text-3xl md:text-4xl font-light mb-6">
            Interested in Working Together?
          </h2>
          <p className="text-lg text-gray-300 mb-8 max-w-2xl mx-auto">
            Let's discuss how we can bring your vision to life with thoughtful design and creative solutions.
          </p>
          
          <button 
            onClick={() => {
              if (portfolioData?.personal?.email) {
                window.location.href = `mailto:${portfolioData.personal.email}`;
              }
            }}
            className="bg-white text-gray-900 px-8 py-4 rounded-full font-medium hover:bg-gray-100 transition-colors duration-200 text-lg"
          >
            Get In Touch
          </button>
        </div>
      </section>
    </div>
  );
};

export default ProjectDetail;