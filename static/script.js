// Hide the loading overlay once the page is fully loaded
window.onload = function() {
    const loadingOverlay = document.querySelector('.loading-overlay');
    loadingOverlay.style.display = 'none'; // Hide the loading overlay
};

function contactMember(email) {
    window.location.href = `mailto:${email}`;
}
// Initialize AOS (Animate On Scroll) Library
document.addEventListener("DOMContentLoaded", function () {
    AOS.init({
        duration: 1000,  // Animation duration
        once: true       // Animation plays once when visible
    });
});


function goToSection(sectionId) {
    document.getElementById(sectionId).scrollIntoView({ behavior: "instant" });
}

function goToServiceSection(cardId) {
    // First, navigate to the Services section
    document.getElementById("services").scrollIntoView({ behavior: "instant" });

    // Then, wait a bit and navigate to the specific card
    setTimeout(() => {
        document.getElementById(cardId).scrollIntoView({ behavior: "instant" });
    }, 200); // Small delay to ensure smooth navigation
}

//image recogniton
function goToServiceSection(serviceId) {
    let section = document.getElementById(serviceId);
    if (section) {
        section.scrollIntoView({ behavior: "smooth" });

        // Close dropdown after clicking
        let dropdown = document.querySelector(".dropdown-menu.show");
        if (dropdown) {
            dropdown.classList.remove("show");
        }
    } else {
        console.error("Service section not found:", serviceId);
    }
}

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

