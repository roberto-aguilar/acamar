Acamar
===========
[![Build Status](https://travis-ci.org/DojoGeek/Acamar.svg?branch=master)](https://travis-ci.org/DojoGeek/Acamar)
[![Coverage Status](https://coveralls.io/repos/DojoGeek/Acamar/badge.svg?branch=master)](https://coveralls.io/r/DojoGeek/Acamar?branch=master)

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

Before each commit, run the following script and ensure that no problems were detected

```sh
sh tests.sh
```
