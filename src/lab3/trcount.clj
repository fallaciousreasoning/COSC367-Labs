(defn my-tr-count
  ([lst] (my-tr-count lst 0))
  ([lst accumulator ] (
    if (= lst()) accumulator
                        (recur (rest lst) (+ accumulator 1))

                                                                    )))
(println (my-tr-count '(3 "Fred" :key 23.0)))
(println (my-tr-count () 0))
(println (my-tr-count (range 2) 0))
(println (my-tr-count (range 5) 5))
(println (my-tr-count (range 7)))
(println (my-tr-count ()))
(println (map my-tr-count (list (range 3) (range 6) (range 7))))