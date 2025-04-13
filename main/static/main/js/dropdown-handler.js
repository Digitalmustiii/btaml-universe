// Dropdown Menu Handler Module
const DropdownHandler = {
    init: function() {
      this.dropdownItems = document.querySelectorAll('.navbar li');
      this.setupDropdowns();
    },
    
    setupDropdowns: function() {
      this.dropdownItems.forEach(item => {
        const dropdownLink = item.querySelector('a.has-dropdown');
        const dropdownMenu = item.querySelector('.dropdown-menu');
        
        // Only add event handlers to items with dropdowns
        if (dropdownLink && dropdownMenu) {
          // For mobile view, prevent the link from navigating and toggle dropdown instead
          dropdownLink.addEventListener('click', (e) => {
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
          
          // For desktop view, add hover class
          item.addEventListener('mouseenter', function() {
            if (window.innerWidth > 900) {
              this.classList.add('dropdown-active');
            }
          });
          
          item.addEventListener('mouseleave', function() {
            if (window.innerWidth > 900) {
              this.classList.remove('dropdown-active');
            }
          });
        }
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