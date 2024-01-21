function generateRandomName() {
    const adjectives = ["Purple", "Happy", "Mighty", "Laughing", "Quiet"];
    const nouns = ["Goat", "Penguin", "Tiger", "Rabbit", "Eagle"];
    const adjective = adjectives[Math.floor(Math.random() * adjectives.length)];
    const noun = nouns[Math.floor(Math.random() * nouns.length)];
    document.getElementById("randomName").value = adjective + " " + noun;
}

document.getElementById('uploadButton').addEventListener('click', function () {
    document.getElementById('photoUpload').click();
});

function toggleDropdown(event) {
    // Stop the event from propagating to the document
    event.stopPropagation();

    var dropdownItems = document.querySelector('.dropdown-items');
    var isDisplayed = dropdownItems.style.display === 'block';

    // Hide any other open dropdowns
    document.querySelectorAll('.dropdown-items').forEach(function (dropdown) {
        dropdown.style.display = 'none';
    });

    // Toggle the current dropdown
    dropdownItems.style.display = isDisplayed ? 'none' : 'block';
}

// Close dropdown when clicking outside
window.addEventListener('click', function (event) {
    document.querySelectorAll('.dropdown-items').forEach(function (dropdown) {
        dropdown.style.display = 'none';
    });
});

// Add click event listener to the dropdown anchor
document.querySelector('.dropdown-anchor').addEventListener('click', toggleDropdown);
