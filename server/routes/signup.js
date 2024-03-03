const express=require('express');
const signupUser = require('../controllers/usercontroller.js');
const loginUser = require('../controllers/usercontroller.js');

const router=express.Router();


router.post('/signup',signupUser);
router.post('/login',loginUser);


module.exports = router;
