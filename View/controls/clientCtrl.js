angular.module("yoFeul")
    .controller("clientCtrl", function ($scope, loginService) {
        this.lg = loginService;

    })

var mod = angular.module("yoFeul")

mod.controller("loginCtrl", function ($scope, loginService) {
    var self = this;
    this.error = ""
    this.login = function (user, pass) {
        //user = 'username_01'
        //pass = 'password_01'
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
                    self.error = 'wrong';

                } else {
                    lg.username = user;
                    console.log("IM HERE: " + lg.username);
                    lg.password = pass;
                    lg.key = data.key
                    lg.id = data.id
                    lg.type = data.type;
                    lg.loggedIn = true;
                    $scope.loggedIn = true;
                    $scope.updateName();
                    
                    switch(data.type){
                        case 'client':window.location = '#!user/history';
                        break;
                        case 'agent':
                        window.location = '#!agent/requests';
                        break;
                        case 'manager':
                        window.location = '#!agent/requests';
                        break;
                    }
                
                }
            },
            function (response) {
                self.error = 'wrong';
                console.log('failed responce');
                console.log(response);
            }
        );
    }

});

mod.controller('registerCtrl', function ($scope, registerService) {
    var self = this;
    this.error = "";
    this.msg = "";
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
                    self.error = 'wrong'
                    self.msg = data.error
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
        this.quote_state = 'initial';
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
    this.order_state = 'initial';
    this.Order = function (id) {
        var promise = s('createInvoice', { 'quote_id': id });
        console.log(id);
        promise.then(
            function (response) {
                console.log('successful response');
                console.log(response);
                data = response.data;
                if ('error' in data) {
                    console.log(data.error)
                } else {
                    console.log('invoice was created.');
                    self.order_state = 'done';
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

    this.Pay = function (id) {
        var promise = send('Pay', {'invoice_id': id});

        promise.then(
            function (response) {
                console.log('successful response');
                console.log(response);
                data = response.data;
                if ('error' in data) {
                    console.log(data.error)
                } else {
                    console.log('pay response recieved.');
                    $scope.info.kappa = data;
                    self.getInvoices();
                }
            },
            function (response) {
                console.log('failed response');
                console.log(response);
            }
        );
    }

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

mod.controller('requestCtrl', function ($scope, requestService) {
    var self = this;
    var send = requestService.send;

    this.getRequests = function () {

        var promise = send('getRequestList', {});

        promise.then(
            function (response) {
                console.log('successful response');
                console.log(response);
                data = response.data;
                if ('error' in data) {
                    console.log(data.error)
                } else {
                    console.log('requests were recieved.');
                    $scope.info.requests = data;
                }
            },
            function (response) {
                console.log('failed response');
                console.log(response);
            }
        );
    }

    this.getRequests();

    this.Process = function (id) {

        var promise = send('processOrder', { 'invoice_id': id });

        promise.then(
            function (response) {
                console.log('successful response');
                console.log(response);
                data = response.data;
                if ('error' in data) {
                    console.log(data.error)
                } else {
                    console.log('process response were recieved.');
                    $scope.info.requests = data;
                    self.getRequests();
                }
            },
            function (response) {
                console.log('failed response');
                console.log(response);
            }
        );
    }

});

mod.controller('reportCtrl', function ($scope, requestService, loginService) {
    var self = this;
    var send = requestService.send;

    this.getReport = function () {

        var promise = send('getAllTransactionHistory', {});

        promise.then(
            function (response) {
                console.log('successful response');
                console.log(response);
                data = response.data;
                if ('error' in data) {
                    console.log(data.error)
                } else {
                    console.log('report was recieved.');
                    $scope.info.report = data;
                }
            },
            function (response) {
                console.log('failed response');
                console.log(response);
            }
        );
    }

    this.getReport();

});

mod.controller('rateCtrl', function ($scope, requestService, loginService) {
    var self = this;
    var send = requestService.send;

    this.getRate = function () {

        var promise = send('getRate', {});

        promise.then(
            function (response) {
                console.log('successful response');
                console.log(response);
                data = response.data;
                if ('error' in data) {
                    console.log(data.error)
                } else {
                    console.log('rate was recieved.');
                    $scope.info.rate = data['rate'];
                }
            },
            function (response) {
                console.log('failed response');
                console.log(response);
            }
        );
    }

    this.getRate();

    this.setRate = function () {

        var promise = send('setRate', {'rate': $scope.info.rate});

        promise.then(
            function (response) {
                console.log('successful response');
                console.log(response);
                data = response.data;
                if ('error' in data) {
                    console.log(data.error)
                } else {
                    console.log('setrate response was recieved.');
                }
            },
            function (response) {
                console.log('failed response');
                console.log(response);
            }
        );
    }

});