; lisp practice: http://www.ic.unicamp.br/~meidanis/courses/mc336/2006s2/funcional/L-99_Ninety-Nine_Lisp_Problems.html

; tester

(defun tst(fn ans &rest inp)
  (if (equal (apply fn inp) ans)
    "working"
    (progn
      (princ (apply fn inp))
      (princ " != ")
      (princ ans)
      "broken"
    )
  )
)


; P01 last in list
(defun my-last(lst)
  (car (reverse lst))
)
(tst #'my-last 'd '(a b c d))

; P02 last two
(defun last-two(lst)
  (cdr (cdr lst))
)
(tst #'last-two '(c d) '(a b c d))

; P03 k'th element of list
(defun at(lst n)
  (if (= n 1)
    (car lst)
    (at (cdr lst) (- n 1))
  )
)
(tst #'at 'c '(a b c d e) 3)

; P04 number of elements in list
(defun num-elems(lst)
  (length lst)
)
(tst #'num-elems 4 '(a b c d))

; P05 reverse list
(defun rev-list(lst)
  (reverse lst)
)
(tst #'rev-list '(c b a) '(a b c))

; P06 is palindrome?
(defun is-palindrome(str)
  (equal str (reverse str))
)
(tst #'is-palindrome t "abba")
(tst #'is-palindrome nil "cbba")

; P07 flatten list
(defun flatten-list(lst)
  (let ((b (car lst)) (e (cdr lst)))
    (if (listp b) (setq b (flatten-list b)))
    (if (not (listp b)) (setq b (list b)))
    (if e
      (append b (flatten-list e))
      b
    )
  )
)
(tst #'flatten-list '(a b c d e) '((a) (b c) (d (e))))

; P08 remove consecutive duplicates
(defun remove-dupes(lst)
  (let ( (fst (car lst)) (snd (car (cdr lst))) (rst (cdr (cdr lst))) )
    (if (and fst (equal fst snd))
      (append (list fst) (remove-dupes rst))
      (append (list fst) (remove-dupes (append (list snd) rst)))
    )
  )
)
(tst #'remove-dupes '(a b c) '(a a a b b c))







; factorial

(defun fact(x)
  (if (= x 1)
    1
    (* x (fact (- x 1)))
  )
)

(tst #'fact 7 5040)


; fibonacci

(defun fib(x)
  (if (or (= x 1) (= x 0))
    1
    (+ (fib (- x 1)) (fib (- x 2)))
  )
)

(tst #'fib 34 8)
