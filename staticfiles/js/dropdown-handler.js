// Dropdown Menu Handler Module
const DropdownHandler = {
  init: function() {
    this.dropdownItems = document.querySelectorAll('.navbar li');
    this.setupDropdowns();
    this.handleResize();
  },
    
  setupDropdowns: function() {
    this.dropdownItems.forEach(item => {
      const dropdownLink = item.querySelector('a.has-dropdown');
      const dropdownMenu = item.querySelector('.dropdown-menu');
            
      // Only add event handlers to items with dropdowns
      if (dropdownLink && dropdownMenu) {
        // Remove any existing click event listeners first
        const newDropdownLink = dropdownLink.cloneNode(true);
        dropdownLink.parentNode.replaceChild(newDropdownLink, dropdownLink);
        
        // Add click event for all viewports (mobile and desktop)
        newDropdownLink.addEventListener('click', (e) => {
          if (window.innerWidth <= 900) {
            e.preventDefault();
            e.stopPropagation(); // Prevent event bubbling
                    
            // Close all other open dropdowns first
            this.dropdownItems.forEach(otherItem => {
              if (otherItem !== item && otherItem.classList.contains('dropdown-active')) {
                otherItem.classList.remove('dropdown-active');
              }
            });
                    
            // Toggle this dropdown
            item.classList.toggle('dropdown-active');
          }
        });
                
        // For desktop view, handle hover
        if (window.innerWidth > 900) {
          item.addEventListener('mouseenter', function() {
            this.classList.add('dropdown-active');
          });
                
          item.addEventListener('mouseleave', function() {
            this.classList.remove('dropdown-active');
          });
        }
      }
    });
  },
    
  // Handle resize events to properly switch between mobile and desktop behavior
  handleResize: function() {
    let resizeTimer;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => {
        // Clear event listeners and reinitialize
        this.dropdownItems.forEach(item => {
          item.classList.remove('dropdown-active');
        });
        this.setupDropdowns();
        MobileMenu.resetMobileMenu();
      }, 250);
    });
  },
    
  closeAllDropdowns: function() {
    this.dropdownItems.forEach(item => {
      if (item.classList.contains('dropdown-active')) {
        item.classList.remove('dropdown-active');
      }
    });
  }
};

// Initialize both modules when the DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  MobileMenu.init();
  DropdownHandler.init();
  
  // Specific fix for Business and Investment dropdown
  // Use a more reliable selector that works in vanilla JS
  const businessLinks = document.querySelectorAll('.navbar li a[href*="business"]');
  let businessDropdown = null;
  
  // Find the Business and Investment link
  for (const link of businessLinks) {
    if (link.textContent.includes('Business') || link.textContent.includes('Investment')) {
      businessDropdown = link.closest('li');
      break;
    }
  }
  
  if (businessDropdown) {
    const dropdownLink = businessDropdown.querySelector('a.has-dropdown');
    const dropdownMenu = businessDropdown.querySelector('.dropdown-menu');
    
    if (dropdownLink && dropdownMenu) {
      // Clear any existing event listeners
      const newDropdownLink = dropdownLink.cloneNode(true);
      dropdownLink.parentNode.replaceChild(newDropdownLink, dropdownLink);
      
      // Add specific handler for this dropdown
      newDropdownLink.addEventListener('click', function(e) {
        if (window.innerWidth <= 900) {
          e.preventDefault();
          e.stopPropagation(); // Prevent event bubbling
          
          // First close all dropdowns to avoid conflicts
          document.querySelectorAll('.navbar li.dropdown-active').forEach(item => {
            if (item !== businessDropdown) {
              item.classList.remove('dropdown-active');
            }
          });
          
          // Toggle this dropdown specifically
          businessDropdown.classList.toggle('dropdown-active');
          
          // Add specific positioning for this dropdown to prevent layout shifts
          if (businessDropdown.classList.contains('dropdown-active')) {
            dropdownMenu.style.position = 'static';
            dropdownMenu.style.width = '100%';
            dropdownMenu.style.overflowY = 'auto';
            dropdownMenu.style.maxHeight = '300px'; // Limit height to prevent pushing content too far
          }
        }
      });
    }
  }
});