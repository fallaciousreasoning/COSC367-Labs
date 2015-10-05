(def my-filter (fn [predicate, lst] (
                                      cond (= lst()) ()
                                      (predicate (first lst)) (cons (first lst) (my-filter predicate (rest lst)))
                                      :else (my-filter predicate (rest lst))
                        )))

(println (my-filter even? (range 7)))
(println (my-filter #(= (mod % 3) 0) (range 7)))
(println (my-filter identity '(true false () nil 55 :key "hi")))
