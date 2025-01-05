// This function toggles the visibility of the dropdown menu when the button is clicked

/* Dropdown menu for users to navigate */ 
function toggleMenu() {
    var menu = document.getElementById("dropdownList");
    // Toggle the 'visible' class to show or hide the menu
    menu.classList.toggle("visible");
};

/* Dropdown menu for users to see account status/login/signup */ 
function toggleAccountMenu() {
    var menu = document.getElementById("account-dropdown");
    // Toggle the 'visible' class to show or hide the menu
    menu.classList.toggle("visible");
}