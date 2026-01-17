const tabButtons = document.querySelectorAll('.tab-btn');
const tabContents = ['just', 'popular', 'tv', 'free'];

function switchTab(selectedId) {
    // Toggle contents
    tabContents.forEach(id => {
        document.getElementById(id).style.display = (id === selectedId) ? 'grid' : 'none';
    });

    // Toggle button active state
    tabButtons.forEach(btn => {
        if (btn.id === selectedId + '_tab') {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
}

tabButtons.forEach(btn => {
    btn.onclick = () => {
        const id = btn.id.replace('_tab', '');
        switchTab(id);
    };
});

// Initialize
switchTab('just');

// Mobile Menu Toggle
const mobileToggle = document.querySelector('.mobile-toggle');
const mainNav = document.querySelector('.main-nav');

if (mobileToggle && mainNav) {
    mobileToggle.addEventListener('click', () => {
        mainNav.classList.toggle('active');

        // Toggle hamburger icon animation
        const svg = mobileToggle.querySelector('svg');
        if (mainNav.classList.contains('active')) {
            svg.innerHTML = '<line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line>';
        } else {
            svg.innerHTML = '<line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line>';
        }
    });
}
