from rx.observable import Observable
from rx.testing import TestScheduler, ReactiveTest

on_next = ReactiveTest.on_next
on_completed = ReactiveTest.on_completed
on_error = ReactiveTest.on_error
subscribe = ReactiveTest.subscribe
subscribed = ReactiveTest.subscribed
disposed = ReactiveTest.disposed
created = ReactiveTest.created

def test_skip_complete_after():
    scheduler = TestScheduler()
    xs = scheduler.create_hot_observable(on_next(70, 6), on_next(150, 4), on_next(210, 9), on_next(230, 13), on_next(270, 7), on_next(280, 1), on_next(300, -1), on_next(310, 3), on_next(340, 8), on_next(370, 11), on_next(410, 15), on_next(415, 16), on_next(460, 72), on_next(510, 76), on_next(560, 32), on_next(570, -100), on_next(580, -3), on_next(590, 5), on_next(630, 10), on_completed(690))
    
    def factory():
        return xs.skip(20)
    results = scheduler.start_with_create(factory)
    
    results.messages.assert_equal(on_completed(690))
    xs.subscriptions.assert_equal(subscribe(200, 690))


def test_skip_complete_same():
    scheduler = TestScheduler()
    xs = scheduler.create_hot_observable(on_next(70, 6), on_next(150, 4), on_next(210, 9), on_next(230, 13), on_next(270, 7), on_next(280, 1), on_next(300, -1), on_next(310, 3), on_next(340, 8), on_next(370, 11), on_next(410, 15), on_next(415, 16), on_next(460, 72), on_next(510, 76), on_next(560, 32), on_next(570, -100), on_next(580, -3), on_next(590, 5), on_next(630, 10), on_completed(690))
    
    def factory():
        return xs.skip(17)
    results = scheduler.start_with_create(factory)
    
    results.messages.assert_equal(on_completed(690))
    xs.subscriptions.assert_equal(subscribe(200, 690))


def test_skip_complete_before():
    scheduler = TestScheduler()
    xs = scheduler.create_hot_observable(on_next(70, 6), on_next(150, 4), on_next(210, 9), on_next(230, 13), on_next(270, 7), on_next(280, 1), on_next(300, -1), on_next(310, 3), on_next(340, 8), on_next(370, 11), on_next(410, 15), on_next(415, 16), on_next(460, 72), on_next(510, 76), on_next(560, 32), on_next(570, -100), on_next(580, -3), on_next(590, 5), on_next(630, 10), on_completed(690))
    
    def factory():
        return xs.skip(10)
    results = scheduler.start_with_create(factory)
    
    results.messages.assert_equal(on_next(460, 72), on_next(510, 76), on_next(560, 32), on_next(570, -100), on_next(580, -3), on_next(590, 5), on_next(630, 10), on_completed(690))
    xs.subscriptions.assert_equal(subscribe(200, 690))


def test_skip_Complete_zero():
    scheduler = TestScheduler()
    xs = scheduler.create_hot_observable(on_next(70, 6), on_next(150, 4), on_next(210, 9), on_next(230, 13), on_next(270, 7), on_next(280, 1), on_next(300, -1), on_next(310, 3), on_next(340, 8), on_next(370, 11), on_next(410, 15), on_next(415, 16), on_next(460, 72), on_next(510, 76), on_next(560, 32), on_next(570, -100), on_next(580, -3), on_next(590, 5), on_next(630, 10), on_completed(690))
    
    def factory():
        return xs.skip(0)
    results = scheduler.start_with_create(factory)
    
    results.messages.assert_equal(on_next(210, 9), on_next(230, 13), on_next(270, 7), on_next(280, 1), on_next(300, -1), on_next(310, 3), on_next(340, 8), on_next(370, 11), on_next(410, 15), on_next(415, 16), on_next(460, 72), on_next(510, 76), on_next(560, 32), on_next(570, -100), on_next(580, -3), on_next(590, 5), on_next(630, 10), on_completed(690))
    xs.subscriptions.assert_equal(subscribe(200, 690))


def test_skip_error_after():
    ex = 'ex'
    scheduler = TestScheduler()
    xs = scheduler.create_hot_observable(on_next(70, 6), on_next(150, 4), on_next(210, 9), on_next(230, 13), on_next(270, 7), on_next(280, 1), on_next(300, -1), on_next(310, 3), on_next(340, 8), on_next(370, 11), on_next(410, 15), on_next(415, 16), on_next(460, 72), on_next(510, 76), on_next(560, 32), on_next(570, -100), on_next(580, -3), on_next(590, 5), on_next(630, 10), on_error(690, ex))
    
    def factory():
        return xs.skip(20)
    results = scheduler.start_with_create(factory)
    
    results.messages.assert_equal(on_error(690, ex))
    xs.subscriptions.assert_equal(subscribe(200, 690))


def test_skip_error_same():
    ex = 'ex'
    scheduler = TestScheduler()
    xs = scheduler.create_hot_observable(on_next(70, 6), on_next(150, 4), on_next(210, 9), on_next(230, 13), on_next(270, 7), on_next(280, 1), on_next(300, -1), on_next(310, 3), on_next(340, 8), on_next(370, 11), on_next(410, 15), on_next(415, 16), on_next(460, 72), on_next(510, 76), on_next(560, 32), on_next(570, -100), on_next(580, -3), on_next(590, 5), on_next(630, 10), on_error(690, ex))
    
    def factory():
        return xs.skip(17)
    results = scheduler.start_with_create(factory)

    results.messages.assert_equal(on_error(690, ex))
    xs.subscriptions.assert_equal(subscribe(200, 690))


def test_skip_error_before():
    ex = 'ex'
    scheduler = TestScheduler()
    xs = scheduler.create_hot_observable(on_next(70, 6), on_next(150, 4), on_next(210, 9), on_next(230, 13), on_next(270, 7), on_next(280, 1), on_next(300, -1), on_next(310, 3), on_next(340, 8), on_next(370, 11), on_next(410, 15), on_next(415, 16), on_next(460, 72), on_next(510, 76), on_next(560, 32), on_next(570, -100), on_next(580, -3), on_next(590, 5), on_next(630, 10), on_error(690, ex))
    
    def factory():
        return xs.skip(3)
    results = scheduler.start_with_create(factory)
        
    results.messages.assert_equal(on_next(280, 1), on_next(300, -1), on_next(310, 3), on_next(340, 8), on_next(370, 11), on_next(410, 15), on_next(415, 16), on_next(460, 72), on_next(510, 76), on_next(560, 32), on_next(570, -100), on_next(580, -3), on_next(590, 5), on_next(630, 10), on_error(690, ex))
    xs.subscriptions.assert_equal(subscribe(200, 690))


def test_skip_dispose_before():
    scheduler = TestScheduler()
    xs = scheduler.create_hot_observable(on_next(70, 6), on_next(150, 4), on_next(210, 9), on_next(230, 13), on_next(270, 7), on_next(280, 1), on_next(300, -1), on_next(310, 3), on_next(340, 8), on_next(370, 11), on_next(410, 15), on_next(415, 16), on_next(460, 72), on_next(510, 76), on_next(560, 32), on_next(570, -100), on_next(580, -3), on_next(590, 5), on_next(630, 10))
    
    def dispose():
        return xs.skip(3)
    
    results = scheduler.start_with_dispose(dispose, 250)
    results.messages.assert_equal()
    xs.subscriptions.assert_equal(subscribe(200, 250))


def test_skip_dispose_after():
    scheduler = TestScheduler()
    xs = scheduler.create_hot_observable(on_next(70, 6), on_next(150, 4), on_next(210, 9), on_next(230, 13), on_next(270, 7), on_next(280, 1), on_next(300, -1), on_next(310, 3), on_next(340, 8), on_next(370, 11), on_next(410, 15), on_next(415, 16), on_next(460, 72), on_next(510, 76), on_next(560, 32), on_next(570, -100), on_next(580, -3), on_next(590, 5), on_next(630, 10))
    
    def dispose():
        return xs.skip(3)
    results = scheduler.start_with_dispose(dispose, 400)
    results.messages.assert_equal(on_next(280, 1), on_next(300, -1), on_next(310, 3), on_next(340, 8), on_next(370, 11))
    xs.subscriptions.assert_equal(subscribe(200, 400))

