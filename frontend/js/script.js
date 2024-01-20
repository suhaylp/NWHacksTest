function generateRandomName() {
    const adjectives = ["Purple", "Happy", "Mighty", "Laughing", "Quiet", "Crazy"];
    const nouns = ["Goat", "Penguin", "Tiger", "Rabbit", "Eagle", "Elephant", "Crocodile", "Hamster", "Bunny", "Giraffe"];
    const adjective = adjectives[Math.floor(Math.random() * adjectives.length)];
    const noun = nouns[Math.floor(Math.random() * nouns.length)];
    document.getElementById("randomName").value = adjective + " " + noun;
}
document.getElementById('uploadButton').addEventListener('click', function () {
    document.getElementById('photoUpload').click();
});

