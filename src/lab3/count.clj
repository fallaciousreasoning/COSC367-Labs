(def my-count (fn [lst]
           (if (= lst())
             0
             (+ 1 (my-count(rest lst))))))

(println (my-count '(3 "Fred" :key 23.0))) 
(println (my-count (range 7)))
(println (my-count ()))
(println (map my-count (list (range 3) (range 6) (range 7))))