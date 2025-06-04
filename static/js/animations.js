// JavaScript animations and interactions

// Smooth scroll to element
function smoothScrollTo(elementId) {
    document.getElementById(elementId)?.scrollIntoView({
        behavior: 'smooth'
    });
}

// Add sparkle effect to buttons
function addSparkleEffect(element) {
    element.addEventListener('click', function(e) {
        const sparkle = document.createElement('div');
        sparkle.className = 'sparkle';
        sparkle.style.left = e.clientX + 'px';
        sparkle.style.top = e.clientY + 'px';
        document.body.appendChild(sparkle);
        
        setTimeout(() => {
            sparkle.remove();
        }, 1000);
    });
}

// Initialize animations when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Add sparkle effect to all buttons
    document.querySelectorAll('button').forEach(addSparkleEffect);
    
    // Add intersection observer for fade-in animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    });
    
    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });
});