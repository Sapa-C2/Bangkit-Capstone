require('dotenv').config();

const express = require("express");

const app = express();
cont 
const MiddlewareLogsrequest = require('./middleware/logs.js');


app.use(MiddlewareLogsrequest);
app.use(express.json());



app.get("/", (req, res) => {
    res.send("hello")
});


app.listen(4000, () => {
    console.log('Server berhasil di running di port 4000');
})
