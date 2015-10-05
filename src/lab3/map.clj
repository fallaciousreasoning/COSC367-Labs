(def my-map (fn [function, lst] (
                                  if (= lst()) ()
                                  (cons (function (first lst)) (my-map function (rest lst)))
                                  )))
(println (my-map
           (fn [x] (* 10 x))
           (range 5)))
(println (my-map
           even?
           (range 7)))
(my-map println '("Hi COSC367!"))
(println (my-map
           (fn [x] x)
           ()))