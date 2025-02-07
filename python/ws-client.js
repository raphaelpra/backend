const socket = new WebSocket("ws://localhost:8765");

socket.onopen = () => {
    console.log("Connected to server");
    socket.send("Hello, WebSocket! from JS");
    socket.close(1000, "Bye!");
    process.exit(0);
};

socket.onmessage = (event) => {
    console.log(`Received: ${event.data}`);
};

socket.onerror = (error) => {
    console.error(`WebSocket error: ${error}`);
};

socket.onclose = () => {
    console.log("Connection closed");
};
