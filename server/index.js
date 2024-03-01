const express = require('express');
const path = require('path'); // Require path module separately

const app = express();

app.get('/', (req, res) => {
    res.sendFile(path.resolve(__dirname, '../client/src/components/Login/LoginPage.js'));
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Server is listening at port ${PORT}`);
});
