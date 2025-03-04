
import React, { useState } from 'react';
import { Search, Filter } from 'lucide-react';

interface SearchBarProps {
  onSearch: (query: string) => void;
}

const SearchBar: React.FC<SearchBarProps> = ({ onSearch }) => {
  const [query, setQuery] = useState('');
  const [showFilters, setShowFilters] = useState(false);

  const handleSearch = () => {
    onSearch(query);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };

  const toggleFilters = () => {
    setShowFilters(!showFilters);
  };

  return (
    <div className="w-full flex flex-col mb-4">
      <div className="flex items-center space-x-2 w-full">
        <div className="relative flex-1">
          <input
            type="text"
            placeholder="Search for a service..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={handleKeyDown}
            className="w-full px-4 py-2.5 pl-10 rounded-lg border border-gray-300 dark:border-gray-700 focus:outline-none focus:ring-2 focus:ring-scraper-blue dark:bg-gray-800 dark:text-white transition-all duration-300 font-sans shadow-sm"
          />
          <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
            <Search size={18} className="text-gray-400" />
          </div>
        </div>
        <button
          onClick={handleSearch}
          className="px-5 py-2.5 bg-scraper-blue text-white rounded-lg hover:bg-blue-600 transition-colors duration-300 shadow-sm font-medium flex-shrink-0"
        >
          Search
        </button>
        <button
          onClick={toggleFilters}
          className="p-2.5 bg-gray-100 text-gray-700 dark:bg-gray-700 dark:text-white rounded-lg hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors duration-300 shadow-sm flex items-center justify-center flex-shrink-0"
          aria-label="Toggle filters"
        >
          <Filter size={18} />
        </button>
      </div>
      
      {/* Advanced Search Filters */}
      {showFilters && (
        <div className="mt-3 p-3 border border-gray-200 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 shadow-sm animate-fade-in">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
            <div>
              <label className="block text-xs font-medium text-gray-600 dark:text-gray-400 mb-1">Category</label>
              <select className="w-full p-2 rounded border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white">
                <option value="">All Categories</option>
                <option value="network">Network</option>
                <option value="application">Application</option>
                <option value="system">System</option>
              </select>
            </div>
            <div>
              <label className="block text-xs font-medium text-gray-600 dark:text-gray-400 mb-1">Severity</label>
              <select className="w-full p-2 rounded border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white">
                <option value="">Any Severity</option>
                <option value="critical">Critical</option>
                <option value="high">High</option>
                <option value="medium">Medium</option>
                <option value="low">Low</option>
              </select>
            </div>
            <div>
              <label className="block text-xs font-medium text-gray-600 dark:text-gray-400 mb-1">Date Range</label>
              <select className="w-full p-2 rounded border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-white">
                <option value="all">All Time</option>
                <option value="today">Today</option>
                <option value="week">This Week</option>
                <option value="month">This Month</option>
              </select>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default SearchBar;
