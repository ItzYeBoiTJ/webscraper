
import React from 'react';
import { Link } from 'react-router-dom';
import { Moon, Sun, Home, Search, Wifi, Shield, Settings, Bell, Database, Lock } from 'lucide-react';
import { useTheme } from '@/hooks/useTheme';

const Navbar = () => {
  const { theme, toggleTheme } = useTheme();

  return (
    <div className="flex flex-col h-full">
      {/* Logo and Theme Toggle */}
      <div className="flex items-center justify-between">
        <div className="flex items-center">
          <Shield className="text-scraper-blue mr-2" size={22} />
          <h1 className="text-lg font-bold font-heading">WEB SCRAPING TOOL</h1>
        </div>
        <div className="flex items-center space-x-2">
          <button 
            onClick={toggleTheme} 
            className="p-2 rounded-md hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
            aria-label="Toggle theme"
          >
            {theme === 'dark' ? (
              <Sun size={20} className="text-yellow-400" />
            ) : (
              <Moon size={20} className="text-gray-700" />
            )}
          </button>
          <Link 
            to="/login" 
            className="px-4 py-1.5 bg-scraper-blue text-white dark:bg-scraper-blue dark:text-white rounded-md hover:opacity-90 transition-colors font-medium text-sm"
          >
            LOGIN
          </Link>
        </div>
      </div>

      {/* Mobile Navigation */}
      <div className="md:hidden fixed bottom-0 left-0 right-0 bg-white dark:bg-gray-900 border-t border-gray-200 dark:border-gray-700 z-10 shadow-lg">
        <div className="flex justify-around py-3">
          <Link to="/" className="flex flex-col items-center text-gray-600 dark:text-gray-300 hover:text-scraper-blue dark:hover:text-scraper-blue">
            <Home size={20} />
            <span className="text-xs mt-1 font-medium">HOME</span>
          </Link>
          <Link to="/search" className="flex flex-col items-center text-gray-600 dark:text-gray-300 hover:text-scraper-blue dark:hover:text-scraper-blue">
            <Search size={20} />
            <span className="text-xs mt-1 font-medium">SEARCH</span>
          </Link>
          <Link to="/connect" className="flex flex-col items-center text-gray-600 dark:text-gray-300 hover:text-scraper-blue dark:hover:text-scraper-blue">
            <Wifi size={20} />
            <span className="text-xs mt-1 font-medium">CONNECT</span>
          </Link>
        </div>
      </div>

      {/* Sidebar for Desktop - Expanded with more options */}
      <div className="hidden md:flex flex-col h-screen fixed left-0 top-0 bg-white dark:bg-gray-800 w-[240px] p-5 border-r border-gray-200 dark:border-gray-700 shadow-sm">
        <div className="flex items-center mb-8">
          <Shield className="text-scraper-blue mr-2" size={24} />
          <h1 className="font-bold text-lg font-heading">WEB SCRAPER</h1>
        </div>
        
        {/* Primary Navigation */}
        <div className="mb-6">
          <p className="text-xs text-gray-500 uppercase tracking-wider font-semibold mb-3 pl-2">Main Navigation</p>
          <div className="flex flex-col space-y-1">
            <Link to="/" className="flex items-center space-x-3 p-2.5 rounded-md hover:bg-gray-100 dark:hover:bg-gray-700 text-gray-700 dark:text-gray-200 hover:text-scraper-blue dark:hover:text-scraper-blue transition-colors">
              <Home size={20} />
              <span className="font-medium">Home</span>
            </Link>
            <Link to="/search" className="flex items-center space-x-3 p-2.5 rounded-md bg-gray-100 dark:bg-gray-700 text-scraper-blue dark:text-scraper-blue hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors">
              <Search size={20} />
              <span className="font-medium">Search</span>
            </Link>
            <Link to="/connect" className="flex items-center space-x-3 p-2.5 rounded-md hover:bg-gray-100 dark:hover:bg-gray-700 text-gray-700 dark:text-gray-200 hover:text-scraper-blue dark:hover:text-scraper-blue transition-colors">
              <Wifi size={20} />
              <span className="font-medium">Connect</span>
            </Link>
          </div>
        </div>
        
        {/* Analytics Section */}
        <div className="mb-6">
          <p className="text-xs text-gray-500 uppercase tracking-wider font-semibold mb-3 pl-2">Analytics</p>
          <div className="flex flex-col space-y-1">
            <Link to="/dashboard" className="flex items-center space-x-3 p-2.5 rounded-md hover:bg-gray-100 dark:hover:bg-gray-700 text-gray-700 dark:text-gray-200 hover:text-scraper-blue dark:hover:text-scraper-blue transition-colors">
              <Database size={20} />
              <span className="font-medium">Data Explorer</span>
            </Link>
            <Link to="/reports" className="flex items-center space-x-3 p-2.5 rounded-md hover:bg-gray-100 dark:hover:bg-gray-700 text-gray-700 dark:text-gray-200 hover:text-scraper-blue dark:hover:text-scraper-blue transition-colors">
              <Bell size={20} />
              <span className="font-medium">Alerts</span>
            </Link>
          </div>
        </div>
        
        {/* Settings Section */}
        <div className="mt-auto">
          <div className="flex flex-col space-y-1">
            <Link to="/settings" className="flex items-center space-x-3 p-2.5 rounded-md hover:bg-gray-100 dark:hover:bg-gray-700 text-gray-700 dark:text-gray-200 hover:text-scraper-blue dark:hover:text-scraper-blue transition-colors">
              <Settings size={20} />
              <span className="font-medium">Settings</span>
            </Link>
            <Link to="/security" className="flex items-center space-x-3 p-2.5 rounded-md hover:bg-gray-100 dark:hover:bg-gray-700 text-gray-700 dark:text-gray-200 hover:text-scraper-blue dark:hover:text-scraper-blue transition-colors">
              <Lock size={20} />
              <span className="font-medium">Security</span>
            </Link>
          </div>
          
          {/* Theme Toggle in Sidebar */}
          <div className="flex items-center mt-6 px-2">
            <button 
              onClick={toggleTheme}
              className="flex items-center justify-between w-full p-2.5 rounded-md hover:bg-gray-100 dark:hover:bg-gray-700 text-gray-700 dark:text-gray-200 transition-colors"
            >
              <div className="flex items-center">
                {theme === 'dark' ? <Sun size={20} /> : <Moon size={20} />}
                <span className="ml-3 font-medium">{theme === 'dark' ? 'Light Mode' : 'Dark Mode'}</span>
              </div>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
