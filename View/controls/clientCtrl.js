angular.module("yoFeul")
    .controller("clientCtrl", function ($scope, loginService) {
        this.lg = loginService;

    })

var mod = angular.module("yoFeul")

mod.controller("loginCtrl", function ($scope, loginService) {
    this.login = function (user, pass) {
        user = 'username_01'
        pass = 'password_01'
        if (user == undefined) {

            return;
        }
        if (pass == undefined) {

            return;
        }

        var lg = loginService;
        var promise = lg.login(user, pass);

        promise.then(
            function (response) {
                console.log('successful responce');
                console.log(response);
                data = response.data;
                if ('error' in data) {
                    console.log(data.error)
                } else {
                    lg.username = user;
                    console.log("IM HERE: " + lg.username);
                    lg.password = pass;
                    lg.key = data.key
                    lg.id = data.id
                    lg.loggedIn = true;
                    $scope.loggedIn = true;
                    $scope.updateName();

                    window.location = '#!user/history';
                }
            },
            function (response) {
                console.log('failed responce');
                console.log(response);
            }
        );
    }

});

mod.controller('registerCtrl', function ($scope, registerService) {
    this.register = function (user, pass, conf) {
        if (user == undefined) {
            return;
        }
        if (pass == undefined) {
            return;
        }
        if (conf == undefined) {
            return;
        }

        var rs = registerService;
        var promise = rs.register(user, pass, conf);

        promise.then(
            function (response) {
                console.log('successful response');
                console.log(response);
                data = response.data;
                if ('error' in data) {
                    console.log(data.error)
                } else {
                    console.log('registered');
                    window.location = '#!login';
                }
            },
            function (response) {
                console.log('failed responce');
                console.log(response);
            }
        );
    };


});

mod.controller('profileCtrl', function ($scope, requestService, loginService) {
    var self = this;
    var s = requestService.send;
    this.send = function (first, last, company, add1, add2, city, state, zip) {
        var reqdata = {
            'firstname': (first == undefined) ? null : first,
            'lastname': (last == undefined) ? null : last,
            'company': (company == undefined) ? null : company,
            'address1': (add1 == undefined) ? null : add1,
            'address2': (add2 == undefined) ? null : add2,
            'city': (city == undefined) ? null : city,
            'state': (state == undefined) ? null : state,
            'zipcode': (zip == undefined) ? 00000 : zip,
            'key': loginService.key,
            'username': loginService.username
        }
        console.log(reqdata)
        var rs = requestService;
        var promise = rs.send('modifyProfile', reqdata);

        promise.then(
            function (response) {
                console.log('successful response');
                console.log(response);
                data = response.data;
                if ('error' in data) {
                    console.log(data.error)
                } else {
                    console.log('updated');
                    //window.location = '#!login';
                }
            },
            function (response) {
                console.log('failed response');
                console.log(response);
            }
        );
    };

    this.getProfile = function () {

        var promise = s('getProfile', {});

        promise.then(
            function (response) {
                console.log('successful response');
                console.log(response);
                data = response.data;
                if ('error' in data) {
                    console.log(data.error)
                } else {
                    console.log('profile info recieved.');
                    $scope.info.profile = data[0];
                }
            },
            function (response) {
                console.log('failed response');
                console.log(response);
            }
        );
    }

    this.getProfile();

    this.quote_state = 'initial';

    this.getQuote = function (gallons, date, state) {
        var promise = s('getQuote', { 'gallons': gallons, 'date': date, 'state': state });

        promise.then(
            function (response) {
                console.log('successful response');
                console.log(response);
                data = response.data;
                if ('error' in data) {
                    console.log(data.error)
                } else {
                    console.log('quote was recieved.');
                    $scope.info.price = data;
                    self.quote_state = 'quote';
                }
            },
            function (response) {
                console.log('failed response');
                console.log(response);
            }
        );
    }

});

mod.controller('invoiceCtrl', function ($scope, requestService, loginService) {
    var self = this;
    var send = requestService.send;

    this.getInvoices = function () {

        var promise = send('getInvoices', {});

        promise.then(
            function (response) {
                console.log('successful response');
                console.log(response);
                data = response.data;
                if ('error' in data) {
                    console.log(data.error)
                } else {
                    console.log('invoices were recieved.');
                    $scope.info.invoices = data;
                }
            },
            function (response) {
                console.log('failed response');
                console.log(response);
            }
        );
    }

    this.getInvoices();

});

mod.controller('historyCtrl', function ($scope, requestService, loginService) {
    var self = this;
    var send = requestService.send;

    this.getQuotes = function () {

        var promise = send('getQuotes', {});

        promise.then(
            function (response) {
                console.log('successful response');
                console.log(response);
                data = response.data;
                if ('error' in data) {
                    console.log(data.error)
                } else {
                    console.log('quotes were recieved.');
                    $scope.info.quotes = data;
                }
            },
            function (response) {
                console.log('failed response');
                console.log(response);
            }
        );
    }

    this.getQuotes();

});
