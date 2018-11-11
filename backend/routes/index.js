const express = require('express');

const router = express.Router();

router.get('/', (req, res) => {
  res.render('form', {title: 'Registration form'});
});

router.post('/', (req, res) => {
  console.log(req.body.name);
  res.render('result', {title: 'Registration form', name: req.body.name});
});

module.exports = router
