// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Create mobile menu toggle button
    const mobileMenuToggle = document.createElement('button');
    mobileMenuToggle.className = 'mobile-menu-toggle';
    mobileMenuToggle.setAttribute('aria-label', 'Toggle navigation menu');
    mobileMenuToggle.innerHTML = '☰';
    
    // Get header and navbar elements
    const header = document.querySelector('.main-header');
    const navbar = document.querySelector('.navbar');
    const logoContainer = document.querySelector('.logo-container');
    
    // Insert the toggle button after the logo container
    if (header && navbar && logoContainer) {
      header.insertBefore(mobileMenuToggle, navbar);
      
      // Toggle mobile menu when button is clicked
      mobileMenuToggle.addEventListener('click', function() {
        navbar.classList.toggle('active');
        // Change icon based on menu state
        this.innerHTML = navbar.classList.contains('active') ? '✕' : '☰';
      });
    }
    
    // Handle dropdown menus on mobile
    const dropdownItems = document.querySelectorAll('.navbar li');
    
    dropdownItems.forEach(item => {
      const dropdownLink = item.querySelector('a.has-dropdown');
      const dropdownMenu = item.querySelector('.dropdown-menu');
      
      // Only add event handlers to items with dropdowns
      if (dropdownLink && dropdownMenu) {
        // For mobile view, prevent the link from navigating and toggle dropdown instead
        dropdownLink.addEventListener('click', function(e) {
          if (window.innerWidth <= 900) {
            e.preventDefault();
            
            // Close all other open dropdowns first
            dropdownItems.forEach(otherItem => {
              if (otherItem !== item && otherItem.classList.contains('dropdown-active')) {
                otherItem.classList.remove('dropdown-active');
              }
            });
            
            // Toggle this dropdown
            item.classList.toggle('dropdown-active');
          }
        });
      }
    });
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(e) {
      if (navbar && navbar.classList.contains('active') && 
          !navbar.contains(e.target) && 
          !mobileMenuToggle.contains(e.target)) {
        navbar.classList.remove('active');
        mobileMenuToggle.innerHTML = '☰';
        
        // Also close any open dropdowns
        dropdownItems.forEach(item => {
          if (item.classList.contains('dropdown-active')) {
            item.classList.remove('dropdown-active');
          }
        });
      }
    });
    
    // Close mobile menu on window resize to desktop size
    window.addEventListener('resize', function() {
      if (window.innerWidth > 900) {
        if (navbar && navbar.classList.contains('active')) {
          navbar.classList.remove('active');
        }
        if (mobileMenuToggle) {
          mobileMenuToggle.innerHTML = '☰';
        }
        
        // Close all dropdowns too
        dropdownItems.forEach(item => {
          if (item.classList.contains('dropdown-active')) {
            item.classList.remove('dropdown-active');
          }
        });
      }
    });
    
    // Fix for larger dropdown menus to ensure they stay on screen
    window.addEventListener('load', adjustDropdownPositions);
    window.addEventListener('resize', adjustDropdownPositions);
    
    function adjustDropdownPositions() {
      if (window.innerWidth > 900) {
        const dropdownMenus = document.querySelectorAll('.dropdown-menu');
        
        dropdownMenus.forEach(menu => {
          // Reset position first
          menu.style.left = '0';
          
          // Check if menu goes off-screen
          const rect = menu.getBoundingClientRect();
          if (rect.right > window.innerWidth) {
            // Adjust position to stay on screen
            menu.style.left = 'auto';
            menu.style.right = '0';
          }
        });
      }
    }
  });