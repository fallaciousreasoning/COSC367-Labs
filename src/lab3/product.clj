(defn product [lst] (
                      apply * lst
                      ))
(println (product '(5 4 33)))

(def my-list '((3/4 3/4) (7/17 1/2) (0.2 0.5) () (91) (1 0 77)))
(println (map product my-list))