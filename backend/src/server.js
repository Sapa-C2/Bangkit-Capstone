require('dotenv').config();

const express = require("express");

const app = express();
const stageRoutes = require('./routes/stage.js');
const MiddlewareLogsrequest = require('./middleware/logs.js');


app.use(MiddlewareLogsrequest);
app.use(express.json());

app.use('/stage', stageRoutes);

app.get("/", (req, res) => {
    res.send("hello")
});


app.listen(4000, () => {
    console.log('Server berhasil di running di port 4000');
})
