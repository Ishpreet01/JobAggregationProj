const express=require('express');
const signupUser = require('../controllers/signupcontroller.js');
const loginUser = require('../controllers/logincontroller.js');
const scrapeHandler = require('../controllers/scrapecontroller.js');


const router=express.Router();


router.post('/signup',signupUser);
router.post('/login',loginUser);
router.get('/scrape',scrapeHandler);


module.exports = router;
