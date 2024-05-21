const express = require("express");
const app = express();
const usersRoutes = require('./routes/users.js');


app.use('/users', usersRoutes);

app.get("/", (req, res) => {
    res.send("hello")
});

app.listen(4000, () => {
    console.log("Server running in port 4000");
});
