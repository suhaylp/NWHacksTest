function generateRandomName() {
    const adjectives = ["Purple", "Happy", "Mighty", "Laughing", "Quiet"];
    const nouns = ["Goat", "Penguin", "Tiger", "Rabbit", "Eagle"];
    const adjective = adjectives[Math.floor(Math.random() * adjectives.length)];
    const noun = nouns[Math.floor(Math.random() * nouns.length)];
    document.getElementById("randomName").value = adjective + " " + noun;
}
