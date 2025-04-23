// Responsive Layout Module
const ResponsiveLayout = {
    init: function() {
      this.setupResizeHandler();
      this.adjustDropdownPositions();
      
      // Call adjustment on initial load too
      window.addEventListener('load', () => this.adjustDropdownPositions());
    },
    
    setupResizeHandler: function() {
      window.addEventListener('resize', () => {
        if (window.innerWidth > 900) {
          // Reset mobile menu when switching to desktop
          MobileMenu.resetMobileMenu();
          
          // Close all dropdowns that were opened in mobile mode
          DropdownHandler.closeAllDropdowns();
        }
        
        // Re-adjust dropdown positions
        this.adjustDropdownPositions();
      });
    },
    
    adjustDropdownPositions: function() {
      if (window.innerWidth > 900) {
        const dropdownMenus = document.querySelectorAll('.dropdown-menu');
        
        dropdownMenus.forEach(menu => {
          // Reset position first
          menu.style.left = '0';
          menu.style.right = 'auto';
          
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
  };