
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Shield, ArrowLeft, User, Lock } from 'lucide-react';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // This would connect to your backend for authentication
    console.log('Login attempt with:', { email, password });
    // For now, we'll just simulate a successful login
    alert('Login functionality will be connected to the backend');
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900 px-4">
      <div className="max-w-md w-full">
        <div className="text-center mb-10">
          <Link to="/" className="inline-flex items-center text-blue-500 hover:text-blue-600 mb-4">
            <ArrowLeft size={20} className="mr-2" />
            Back to Home
          </Link>
          
          <div className="flex items-center justify-center mb-2">
            <Shield className="text-scraper-blue mr-2" size={30} />
            <h1 className="text-3xl font-bold text-gray-900 dark:text-white">SCRAPER</h1>
          </div>
          <p className="text-gray-600 dark:text-gray-400">
            Sign in to access the web scraping dashboard
          </p>
        </div>
        
        <div className="bg-white dark:bg-gray-800 p-8 rounded-lg shadow-md">
          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label htmlFor="email" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                Email Address
              </label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <User size={18} className="text-gray-400" />
                </div>
                <input
                  id="email"
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                  className="pl-10 w-full py-2 border border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                  placeholder="your@email.com"
                />
              </div>
            </div>
            
            <div>
              <label htmlFor="password" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                Password
              </label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <Lock size={18} className="text-gray-400" />
                </div>
                <input
                  id="password"
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                  className="pl-10 w-full py-2 border border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                  placeholder="••••••••"
                />
              </div>
            </div>
            
            <div className="flex items-center justify-between">
              <div className="flex items-center">
                <input
                  id="remember_me"
                  type="checkbox"
                  className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                />
                <label htmlFor="remember_me" className="ml-2 block text-sm text-gray-700 dark:text-gray-300">
                  Remember me
                </label>
              </div>
              
              <div className="text-sm">
                <a href="#" className="text-blue-500 hover:text-blue-600">
                  Forgot password?
                </a>
              </div>
            </div>
            
            <div>
              <button
                type="submit"
                className="w-full py-2 px-4 bg-scraper-blue text-white rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors"
              >
                Sign in
              </button>
            </div>
          </form>
          
          <div className="mt-6 text-center text-sm">
            <p className="text-gray-600 dark:text-gray-400">
              Don't have an account?{' '}
              <a href="#" className="text-blue-500 hover:text-blue-600 font-medium">
                Sign up
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
