// Mobile Menu Module
const MobileMenu = {
    init: function() {
      this.createToggleButton();
      this.setupEventListeners();
    },
    
    createToggleButton: function() {
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
        // Position the toggle button correctly
        header.insertBefore(mobileMenuToggle, navbar);
        
        // Store references for later use
        this.mobileMenuToggle = mobileMenuToggle;
        this.navbar = navbar;
      }
    },
    
    setupEventListeners: function() {
      if (!this.mobileMenuToggle || !this.navbar) return;
      
      // Toggle mobile menu when button is clicked
      this.mobileMenuToggle.addEventListener('click', () => {
        this.navbar.classList.toggle('active');
        // Change icon based on menu state
        this.mobileMenuToggle.innerHTML = this.navbar.classList.contains('active') ? '✕' : '☰';
      });
      
      // Close mobile menu when clicking outside
      document.addEventListener('click', (e) => {
        if (this.navbar.classList.contains('active') && 
            !this.navbar.contains(e.target) && 
            !this.mobileMenuToggle.contains(e.target)) {
          this.navbar.classList.remove('active');
          this.mobileMenuToggle.innerHTML = '☰';
          
          // Also close any open dropdowns
          const dropdownItems = document.querySelectorAll('.navbar li.dropdown-active');
          dropdownItems.forEach(item => {
            item.classList.remove('dropdown-active');
          });
        }
      });
    },
    
    resetMobileMenu: function() {
      if (this.navbar && this.navbar.classList.contains('active')) {
        this.navbar.classList.remove('active');
        this.mobileMenuToggle.innerHTML = '☰';
      }
    }
  };