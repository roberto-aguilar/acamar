Acamar
===========
[![Build Status](https://travis-ci.org/DojoGeek/Acamar.svg?branch=master)](https://travis-ci.org/DojoGeek/Acamar)

Open source store management

### Development requirements

* [Vagrant](https://www.vagrantup.com/downloads.html) 1.7.x or greater

### Set up development environment

* Run the following command to setup virtual environment (it may take a while the first time)

```sh
vagrant up
```

* When the virtual environment is ready, establish a connection with the following command

```sh
vagrant ssh
```

* That's all!

### Contributing

Before each commit ensure the following requirements are met

* Run all test with coverage integration
  * All test must run succesfully
  * The coverage average must be above 90%

```sh
coverage run manage.py test && coverage report
```

* Run source code checker
  * There should be no errors reported

```sh
flake8
```
