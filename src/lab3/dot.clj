;(defn dot-product [vec1 vec2] (
;                                if (or (= vec1()) (= vec2())) 0
;                                (+ (* (first vec1) (first vec2)) (dot-product (rest vec1) (rest vec2)))
;                                ))
(defn dot-product [vec1 vec2] (
                                reduce + (map * vec1 vec2)
                                ))

(println (dot-product '(5 4) '(1 2)))
(println (dot-product () ()))
(println (dot-product (range 4) (range 4)))
