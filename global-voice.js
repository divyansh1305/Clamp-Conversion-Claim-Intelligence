// global-voice.js
// This script enables hands-free voice control across the entire website using the Annyang library.

if (typeof annyang !== 'undefined') {
    const globalCommands = {
        'open dashboard': () => {
            console.log('Voice command: open dashboard');
            window.location.href = 'dashboard.html';
        },
        'open smart save': () => {
            console.log('Voice command: open smart save');
            alert('Smart Save module activated via Voice Command.');
            // window.location.href = 'smart-save.html';
        },
        'invest *amount': (amount) => {
            console.log('Voice command: invest', amount);
            alert(`Voice Command Confirmed: Investing ${amount}`);
        },
        'scroll down': () => {
            console.log('Voice command: scroll down');
            window.scrollBy({ top: 500, behavior: 'smooth' });
        },
        'scroll up': () => {
            console.log('Voice command: scroll up');
            window.scrollBy({ top: -500, behavior: 'smooth' });
        },
        'scroll to top': () => {
            console.log('Voice command: scroll to top');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        },
        'go back': () => {
            console.log('Voice command: go back');
             window.history.back();
        },
        'go home': () => {
            console.log('Voice command: go home');
            window.location.href = 'index.html';
        }
    };
    
    // Add commands to annyang
    annyang.addCommands(globalCommands);
    
    // Start listening.
    annyang.start({ autoRestart: true, continuous: false });
    console.log("Global Hands-Free Mode Active. You can now use voice commands like 'open dashboard', 'scroll down', 'invest 100 dollars'.");
} else {
    console.warn("Annyang library not loaded. Global voice commands disabled.");
}
