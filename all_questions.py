# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] = 0.2780719051126377

    # total variables
    lung_cancer_yes = 5
    lung_cancer_no = 5
    lung_cancer_tot = lung_cancer_yes + lung_cancer_no #total number of objects
    entropy_lung_cancer = -(((lung_cancer_yes/lung_cancer_tot) * u.log2(lung_cancer_yes/lung_cancer_tot)) + ((lung_cancer_no/lung_cancer_tot) * u.log2(lung_cancer_no/lung_cancer_tot)))
    

    #entropy for smoking at level 1
    smoking_yes_yes = 4
    smoking_yes_no = 1
    smoking_yes_tot = smoking_yes_yes + smoking_yes_no
    smoking_no_no = 4
    smoking_no_yes = 1
    smoking_no_tot = smoking_no_yes + smoking_no_no
    entropy_smoking_level1 = -(((smoking_yes_tot/lung_cancer_tot) * (((smoking_yes_yes/smoking_yes_tot) * u.log2(smoking_yes_yes/smoking_yes_tot)) + ((smoking_yes_no/smoking_yes_tot) * u.log2(smoking_yes_no/smoking_yes_tot)))) + ((smoking_no_tot/lung_cancer_tot) * (((smoking_no_yes/smoking_no_tot) * u.log2(smoking_no_yes/smoking_no_tot)) + ((smoking_no_no/smoking_no_tot) * u.log2(smoking_no_no/smoking_no_tot)))))
    print("1a - The entropy for smoking at level 1 is: " +str(entropy_smoking_level1))
    info_gain_smoking_level1 = entropy_lung_cancer - entropy_smoking_level1
    print("1a - The information gain for smoking at level 1 is: " +str(info_gain_smoking_level1))

    level1["cough"] = -1.0
    level1["cough_info_gain"] = 0.034851554559677034

    #entropy for cough at level 1
    cough_yes_yes = 4
    cough_yes_no = 3
    cough_yes_tot = cough_yes_yes + cough_yes_no
    cough_no_no = 2
    cough_no_yes = 1
    cough_no_tot = cough_no_yes + cough_no_no
    entropy_cough_level1 = -(((cough_yes_tot/lung_cancer_tot) * (((cough_yes_yes/cough_yes_tot) * u.log2(cough_yes_yes/cough_yes_tot)) + ((cough_yes_no/cough_yes_tot) * u.log2(cough_yes_no/cough_yes_tot)))) + ((cough_no_tot/lung_cancer_tot) * (((cough_no_yes/cough_no_tot) * u.log2(cough_no_yes/cough_no_tot)) + ((cough_no_no/cough_no_tot) * u.log2(cough_no_no/cough_no_tot)))))
    print("1a - The entropy for cough at level 1 is: " +str(entropy_cough_level1))
    info_gain_cough_level1 = entropy_lung_cancer - entropy_cough_level1
    print("1a - The information gain for cough at level 1 is: " +str(info_gain_cough_level1))

    level1["radon"] = -1.0
    level1["radon_info_gain"] = 0.23645279766002802

    #entropy for radon at level 1
    radon_yes_yes = 2
    radon_yes_no = 0
    radon_yes_tot = radon_yes_yes + radon_yes_no
    radon_no_yes = 3
    radon_no_no = 5
    radon_no_tot = radon_no_yes + radon_no_no
    entropy_radon_level1 = -(((radon_yes_tot/lung_cancer_tot) * (((radon_yes_yes/radon_yes_tot) * u.log2(radon_yes_yes/radon_yes_tot)) + ((radon_yes_no/radon_yes_tot) * 0 ))) + ((radon_no_tot/lung_cancer_tot) * (((radon_no_yes/radon_no_tot) * u.log2(radon_no_yes/radon_no_tot)) + ((radon_no_no/radon_no_tot) * u.log2(radon_no_no/radon_no_tot)))))
    print("1a - The entropy for radon at level 1 is: " +str(entropy_radon_level1))
    info_gain_radon_level1 = entropy_lung_cancer - entropy_radon_level1
    print("1a - The information gain for radon at level 1 is: " +str(info_gain_radon_level1))

    level1["weight_loss"] = -1.0
    level1["weight_loss_info_gain"] = 0.02904940554533142

    #entropy for weight_loss at level 1
    weight_yes_yes = 3
    weight_yes_no = 2
    weight_yes_tot = weight_yes_yes + weight_yes_no
    weight_no_yes = 2
    weight_no_no = 3
    weight_no_tot = weight_no_yes + weight_no_no
    entropy_weight_level1 = -(((weight_yes_tot/lung_cancer_tot) * (((weight_yes_yes/weight_yes_tot) * u.log2(weight_yes_yes/weight_yes_tot)) + ((weight_yes_no/weight_yes_tot) * u.log2(weight_yes_no/weight_yes_tot) ))) + ((weight_no_tot/lung_cancer_tot) * (((weight_no_yes/weight_no_tot) * u.log2(weight_no_yes/weight_no_tot)) + ((weight_no_no/weight_no_tot) * u.log2(weight_no_no/weight_no_tot)))))
    print("1a - The entropy for weight loss at level 1 is: " +str(entropy_weight_level1))
    info_gain_weight_level1 = entropy_lung_cancer - entropy_weight_level1
    print("1a - The information gain for weight loss at level 1 is: " +str(info_gain_weight_level1))

    level2_left["smoking"] = -1.0
    level2_left["smoking_info_gain"] = -1.0

    #entropy of left system at level 2
    l2_l_yes = 4
    l2_l_no = 1
    l2_l_tot = l2_l_yes + l2_l_no
    entropy_l2_l = -(((l2_l_yes/l2_l_tot) * u.log2(l2_l_yes/l2_l_tot)) + ((l2_l_no/l2_l_tot) * u.log2(l2_l_no/l2_l_tot)))

    level2_right["smoking"] = -1.0
    level2_right["smoking_info_gain"] = -1.0

    #level 2 smoking right

    level2_left["radon"] = -1.0
    level2_left["radon_info_gain"] = 0.07290559532005603

    #level 2 radon left
    l2_radon_l_yes_yes = 1
    l2_radon_l_yes_no = 0
    l2_radon_l_yes_tot = l2_radon_l_yes_yes + l2_radon_l_yes_no
    l2_radon_l_no_yes = 3
    l2_radon_l_no_no = 1
    l2_radon_l_no_tot = l2_radon_l_no_yes + l2_radon_l_no_no
    entropy_radon_l2_l = -(((l2_radon_l_yes_tot/l2_l_tot) * (((l2_radon_l_yes_yes/l2_radon_l_yes_tot) * u.log2(l2_radon_l_yes_yes/l2_radon_l_yes_tot)) + ((l2_radon_l_yes_no/l2_radon_l_yes_tot) * 0))) + ((l2_radon_l_no_tot/l2_l_tot) * (((l2_radon_l_no_yes/l2_radon_l_no_tot) * u.log2(l2_radon_l_no_yes/l2_radon_l_no_tot)) + ((l2_radon_l_no_no/l2_radon_l_no_tot) * u.log2(l2_radon_l_no_no/l2_radon_l_no_tot)))))
    print("1a - The entropy for radon at level 2 left is: " +str(entropy_radon_l2_l))
    info_gain_radon_l2_l = entropy_l2_l - entropy_radon_l2_l
    print("1a - The information gain for radon at level 2 left is: " +str(info_gain_radon_l2_l))

    level2_left["cough"] = 1.0
    level2_left["cough_info_gain"] = 0.7219280948873623

    #level 2 cought left
    l2_cough_l_yes_yes = 4
    l2_cough_l_yes_no = 0
    l2_cough_l_yes_tot = l2_cough_l_yes_yes + l2_cough_l_yes_no
    l2_cough_l_no_yes = 0
    l2_cough_l_no_no = 1
    l2_cough_l_no_tot = l2_cough_l_no_yes + l2_cough_l_no_no
    entropy_cough_l2_l = -(((l2_cough_l_yes_tot/l2_l_tot) * (((l2_cough_l_yes_yes/l2_cough_l_yes_tot) * u.log2(l2_cough_l_yes_yes/l2_cough_l_yes_tot)) + ((l2_cough_l_yes_no/l2_cough_l_yes_tot) * 0))) + ((l2_cough_l_no_tot/l2_l_tot) * (((l2_cough_l_no_yes/l2_cough_l_no_tot) * 0) + ((l2_cough_l_no_no/l2_cough_l_no_tot) * u.log2(l2_cough_l_no_no/l2_cough_l_no_tot)))))
    print("1a - The entropy for cough at level 2 left is: " +str(entropy_cough_l2_l))
    info_gain_cough_l2_l = entropy_l2_l - entropy_cough_l2_l
    print("1a - The information gain for cough at level 2 left is: " +str(info_gain_cough_l2_l))
    
    level2_left["weight_loss"] = -1.0
    level2_left["weight_loss_info_gain"] = 0.17095059445466865

    #level 2 weight loss left
    l2_weight_l_yes_yes = 2
    l2_weight_l_yes_no = 0
    l2_weight_l_yes_tot = l2_weight_l_yes_yes + l2_weight_l_yes_no
    l2_weight_l_no_yes = 2
    l2_weight_l_no_no = 1
    l2_weight_l_no_tot = l2_weight_l_no_yes + l2_weight_l_no_no
    entropy_weight_l2_l = -(((l2_weight_l_yes_tot/l2_l_tot) * (((l2_weight_l_yes_yes/l2_weight_l_yes_tot) * u.log2(l2_weight_l_yes_yes/l2_weight_l_yes_tot)) + ((l2_weight_l_yes_no/l2_weight_l_yes_tot) * 0))) + ((l2_weight_l_no_tot/l2_l_tot) * (((l2_weight_l_no_yes/l2_weight_l_no_tot) * (u.log2(l2_weight_l_no_yes/l2_weight_l_no_tot))) + ((l2_weight_l_no_no/l2_weight_l_no_tot) * u.log2(l2_weight_l_no_no/l2_weight_l_no_tot)))))
    print("1a - The entropy for weight loss at level 2 left is: " +str(entropy_weight_l2_l))
    info_gain_weight_l2_l = entropy_l2_l - entropy_weight_l2_l
    print("1a - The information gain for weight loss at level 2 left is: " +str(info_gain_weight_l2_l))

    level2_right["radon"] = 1.0
    level2_right["radon_info_gain"] = 0.7219280948873623

    #level 2 right entropy
    l2_r_yes = 1
    l2_r_no = 4
    l2_r_tot = l2_r_yes + l2_r_no
    entropy_l2_r = -(((l2_r_yes/l2_r_tot) * u.log2(l2_r_yes/l2_r_tot)) + ((l2_r_no/l2_r_tot) * u.log2(l2_r_no/l2_r_tot)))

    #level 2 radon right
    l2_radon_r_yes_yes = 1
    l2_radon_r_yes_no = 0
    l2_radon_r_yes_tot = l2_radon_r_yes_yes + l2_radon_r_yes_no
    l2_radon_r_no_yes = 0
    l2_radon_r_no_no = 4
    l2_radon_r_no_tot = l2_radon_r_no_yes + l2_radon_r_no_no
    entropy_radon_l2_r = -(((l2_radon_r_yes_tot/l2_r_tot) * (((l2_radon_r_yes_yes/l2_radon_r_yes_tot) * u.log2(l2_radon_r_yes_yes/l2_radon_r_yes_tot)) + ((l2_radon_r_yes_no/l2_radon_r_yes_tot) * 0))) + ((l2_radon_r_no_tot/l2_r_tot) * (((l2_radon_r_no_yes/l2_radon_r_no_tot) * 0) + ((l2_radon_r_no_no/l2_radon_r_no_tot) * u.log2(l2_radon_r_no_no/l2_radon_r_no_tot)))))
    print("1a - The entropy for radon at level 2 right is: " +str(entropy_radon_l2_r))
    info_gain_radon_l2_r = entropy_l2_r - entropy_radon_l2_r
    print("1a - The information gain for radon at level 2 right is: " +str(info_gain_radon_l2_r))

    level2_right["cough"] = -1.0
    level2_right["cough_info_gain"] = 0.3219280948873623

    #level 2 cough right
    l2_cough_r_yes_yes = 0
    l2_cough_r_yes_no = 3
    l2_cough_r_yes_tot = l2_cough_r_yes_yes + l2_cough_r_yes_no
    l2_cough_r_no_yes = 1
    l2_cough_r_no_no = 1
    l2_cough_r_no_tot = l2_cough_r_no_yes + l2_cough_r_no_no
    entropy_cough_l2_r = -(((l2_cough_r_yes_tot/l2_r_tot) * (((l2_cough_r_yes_yes/l2_cough_r_yes_tot) * 0) + ((l2_cough_r_yes_no/l2_cough_r_yes_tot) * (u.log2(l2_cough_r_yes_no/l2_cough_r_yes_tot))))) + ((l2_cough_r_no_tot/l2_r_tot) * (((l2_cough_r_no_yes/l2_cough_r_no_tot) * (u.log2(l2_cough_r_no_yes/l2_cough_r_no_tot))) + ((l2_cough_r_no_no/l2_cough_r_no_tot) * u.log2(l2_cough_r_no_no/l2_cough_r_no_tot)))))
    print("1a - The entropy for cough at level 2 right is: " +str(entropy_cough_l2_r))
    info_gain_cough_l2_r = entropy_l2_r - entropy_cough_l2_r
    print("1a - The information gain for cough at level 2 right is: " +str(info_gain_cough_l2_r))

    level2_right["weight_loss"] = -1.0
    level2_right["weight_loss_info_gain"] = 0.17095059445466865

    #level 2 weight loss right
    l2_weight_r_yes_yes = 1
    l2_weight_r_yes_no = 2
    l2_weight_r_yes_tot = l2_weight_r_yes_yes + l2_weight_r_yes_no
    l2_weight_r_no_yes = 0
    l2_weight_r_no_no = 2
    l2_weight_r_no_tot = l2_weight_r_no_yes + l2_weight_r_no_no
    entropy_weight_l2_r = -(((l2_weight_r_yes_tot/l2_r_tot) * (((l2_weight_r_yes_yes/l2_weight_r_yes_tot) * u.log2(l2_weight_r_yes_yes/l2_weight_r_yes_tot)) + ((l2_weight_r_yes_no/l2_weight_r_yes_tot) * (u.log2(l2_weight_r_yes_no/l2_weight_r_yes_tot))))) + ((l2_weight_r_no_tot/l2_r_tot) * (((l2_weight_r_no_yes/l2_weight_r_no_tot) * 0) + ((l2_weight_r_no_no/l2_weight_r_no_tot) * u.log2(l2_weight_r_no_no/l2_weight_r_no_tot)))))
    print("1a - The entropy for weight loss at level 2 right is: " +str(entropy_weight_l2_r))
    info_gain_weight_l2_r = entropy_l2_r - entropy_weight_l2_r
    print("1a - The information gain for weight loss at level 2 right is: " +str(info_gain_weight_l2_r))

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("Smoking")  # MUST STILL CREATE THE TREE *****
    smoking_yes_left = tree.insert_left("Cough") #left split from the root is smoking "YES"
    smoking_no_right = tree.insert_right("Radon")
    smoking_yes_left.insert_left("Yes")
    smoking_yes_left.insert_right("No")
    smoking_no_right.insert_left("Yes")
    smoking_no_right.insert_right("No")

    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    no_of_misplaced_items = 0
    total_items = 10
    training_error = (no_of_misplaced_items/total_items) * 100
    print("1 - The training error is: " +str(training_error))
    answer["training_error"] = 0.0  

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 1.4253642047367425
    #area of a is
    area_a = ((0.3 * 0.3) + (0.8 * 0.4)) 
    area_b = ((0.7 * 0.6) + (0.2 * 0.2)) 
    area_c = ((0.2 * 0.2) + (0.3 * 0.3)) 
    area_total = area_a + area_b + area_c
    entropy_area = -(((area_a) * u.log2(area_a)) + ((area_b) * u.log2(area_b)) + ((area_c) * u.log2(area_c)))
    print("2a - The entropy for the overall data is: " + str(entropy_area))


    # Infogain
    answer["(b) x <= 0.2"] = 0.17739286055515824
    #2-b for x < = 0.2
    area_x_2_l_a = 0
    area_x_2_l_b = ((0.2 * 0.6) + (0.2 * 0.2))
    area_x_2_l_c = (0.2 * 0.2)
    area_x_2_g_a = ((0.8 * 0.4) + (0.3 * 0.3))
    area_x_2_g_b = (0.5 * 0.6)
    area_x_2_g_c = (0.3 * 0.3)
    area_x_2_l_tot = area_x_2_l_a + area_x_2_l_b + area_x_2_l_c
    area_x_2_g_tot = area_x_2_g_a + area_x_2_g_b + area_x_2_g_c
    area_x_2_tot = area_x_2_l_tot + area_x_2_g_tot
    entropy_x_2_l = -(((area_x_2_l_b/area_x_2_l_tot) * (u.log2(area_x_2_l_b/area_x_2_l_tot))) + ((area_x_2_l_c/area_x_2_l_tot) * (u.log2(area_x_2_l_c/area_x_2_l_tot))))
    entropy_x_2_g = -(((area_x_2_g_a/area_x_2_g_tot) * (u.log2(area_x_2_g_a/area_x_2_g_tot))) + ((area_x_2_g_b/area_x_2_g_tot) * (u.log2(area_x_2_g_b/area_x_2_g_tot))) + ((area_x_2_g_c/area_x_2_g_tot) * (u.log2(area_x_2_g_c/area_x_2_g_tot))))
    entropy_x_2 = ((area_x_2_l_tot/area_x_2_tot) * entropy_x_2_l) + ((area_x_2_g_tot/area_x_2_tot) * entropy_x_2_g) 
    entropy_x_2_gain = entropy_area - entropy_x_2
    print("2b - The information gain for split x<= 0.2 is: " + str(entropy_x_2_gain))

    answer["(b) x <= 0.7"] = 0.3557029418697566
    #2-b for x < = 0.7
    area_x_7_l_a = (0.5 * 0.4)
    area_x_7_l_b = ((0.7 * 0.6) + (0.2 * 0.2))
    area_x_7_l_c = (0.2 * 0.2)
    area_x_7_g_a = ((0.3 * 0.4) + (0.3 * 0.3))
    area_x_7_g_b = 0
    area_x_7_g_c = (0.3 * 0.3)
    area_x_7_l_tot = area_x_7_l_a + area_x_7_l_b + area_x_7_l_c
    area_x_7_g_tot = area_x_7_g_a + area_x_7_g_b + area_x_7_g_c
    area_x_7_tot = area_x_7_l_tot + area_x_7_g_tot
    entropy_x_7_l = -(((area_x_7_l_a/area_x_7_l_tot) * (u.log2(area_x_7_l_a/area_x_7_l_tot))) + ((area_x_7_l_b/area_x_7_l_tot) * (u.log2(area_x_7_l_b/area_x_7_l_tot))) + ((area_x_7_l_c/area_x_7_l_tot) * (u.log2(area_x_7_l_c/area_x_7_l_tot))))
    entropy_x_7_g = -(((area_x_7_g_a/area_x_7_g_tot) * (u.log2(area_x_7_g_a/area_x_7_g_tot))) + ((area_x_7_g_c/area_x_7_g_tot) * (u.log2(area_x_7_g_c/area_x_7_g_tot))))
    entropy_x_7 = ((area_x_7_l_tot/area_x_7_tot) * entropy_x_7_l) + ((area_x_7_g_tot/area_x_7_tot) * entropy_x_7_g) 
    entropy_x_7_gain = entropy_area - entropy_x_7
    print("2b - The information gain for split x<= 0.7 is: " + str(entropy_x_7_gain))

    answer["(b) y <= 0.6"] = 0.34781842724338197
    #2-b for y < = 0.6
    area_y_6_l_a = (0.3 * 0.3)
    area_y_6_l_b = (0.7 * 0.6) 
    area_y_6_l_c = (0.3 * 0.3)
    area_y_6_g_a = (0.8 * 0.4)
    area_y_6_g_b = (0.2 * 0.2)
    area_y_6_g_c = (0.2 * 0.2)
    area_y_6_l_tot = area_y_6_l_a + area_y_6_l_b + area_y_6_l_c
    area_y_6_g_tot = area_y_6_g_a + area_y_6_g_b + area_y_6_g_c
    area_y_6_tot = area_y_6_l_tot + area_y_6_g_tot
    entropy_y_6_l = -(((area_y_6_l_a/area_y_6_l_tot) * (u.log2(area_y_6_l_a/area_y_6_l_tot))) + ((area_y_6_l_b/area_y_6_l_tot) * (u.log2(area_y_6_l_b/area_y_6_l_tot))) + ((area_y_6_l_c/area_y_6_l_tot) * (u.log2(area_y_6_l_c/area_y_6_l_tot))))
    entropy_y_6_g = -(((area_y_6_g_a/area_y_6_g_tot) * (u.log2(area_y_6_g_a/area_y_6_g_tot))) + ((area_y_6_g_b/area_y_6_g_tot) * (u.log2(area_y_6_g_b/area_y_6_g_tot))) + ((area_y_6_g_c/area_y_6_g_tot) * (u.log2(area_y_6_g_c/area_y_6_g_tot))))
    entropy_y_6 = ((area_y_6_l_tot/area_y_6_tot) * entropy_y_6_l) + ((area_y_6_g_tot/area_y_6_tot) * entropy_y_6_g) 
    entropy_y_6_gain = entropy_area - entropy_y_6
    print("2b - The information gain for split y<= 0.6 is: " + str(entropy_y_6_gain))

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "x=0.7"  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("x <= 0.7")
    A = tree.insert_left("y <= 0.6")
    B = tree.insert_right("y <= 0.3")
    C = A.insert_right ("x <= 0.2")
    A.insert_left("B")
    B.insert_left("A")
    B.insert_right("A")
    C.insert_right("A")
    D = C.insert_left("y <= 0.8")
    D.insert_left("C")
    D.insert_right("D")


    answer["(d) full decision tree"] = tree
    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5
    #calculating the overall gini
    no_c0_class = 10
    no_c1_class = 10
    no_class_tot = no_c0_class + no_c1_class
    gini_class_total = (1 - (((no_c0_class/no_class_tot)**2) + ((no_c1_class/no_class_tot)**2)))
    print("3a - The gini for overall collection is: " + str(gini_class_total))

    # float
    answer["(b) Gini, ID"] = 0.0
    #Gini will be zero because each customer ID is unique

    answer["(c) Gini, Gender"] = 0.48
    # calculating gini for gender
    no_males_c0 = 6 #number of males in c0
    no_females_c0 = 4 #number of females in c0
    no_males_c1 = 4 #number of males in c1
    no_females_c1 = 6 #number of females in c1
    no_males_tot = no_males_c0 + no_males_c1
    no_females_tot = no_females_c0 + no_females_c1
    gini_males = (1 - (((no_males_c0/no_males_tot)**2) + ((no_males_c1/no_males_tot)**2)))
    gini_females = (1 - (((no_females_c0/no_females_tot)**2) + ((no_females_c1/no_females_tot)**2)))
    no_gender_tot = no_males_tot + no_females_tot
    gini_gender = ((no_males_tot/no_gender_tot) * gini_males) + ((no_females_tot/no_gender_tot) * gini_females)
    print("3c - The gini for gender is: " + str(gini_gender))

    answer["(d) Gini, Car type"] = 0.16250000000000003
    # calculating gini for cartype
    no_family_c0 = 1
    no_family_c1 = 3
    no_family_tot = no_family_c0 + no_family_c1
    no_sports_c0 = 8
    no_sports_c1 = 0
    no_sports_tot = no_sports_c0 + no_sports_c1
    no_luxury_c0 = 1
    no_luxury_c1 = 7
    no_luxury_tot = no_luxury_c0 + no_luxury_c1
    gini_family = (1 - (((no_family_c0/no_family_tot)**2) + ((no_family_c1/no_family_tot)**2)))
    gini_sports = (1 - (((no_sports_c0/no_sports_tot)**2) + ((no_sports_c1/no_sports_tot)**2)))
    gini_luxury = (1 - (((no_luxury_c0/no_luxury_tot)**2) + ((no_luxury_c1/no_luxury_tot)**2)))
    no_car_tot = no_family_tot + no_sports_tot + no_luxury_tot
    gini_cartype = ((no_family_tot/no_car_tot) * gini_family) + ((no_sports_tot/no_car_tot) * gini_sports) + ((no_luxury_tot/no_car_tot) * gini_luxury)
    print("3d - The gini for cartype is: " + str(gini_cartype))

    answer["(e) Gini, Shirt type"] = 0.49142857142857144
    # calulating gini for shirt type
    no_small_c0 = 3
    no_small_c1 = 2
    no_small_tot = no_small_c0 + no_small_c1
    no_medium_c0 = 3
    no_medium_c1 = 4
    no_medium_tot = no_medium_c0 + no_medium_c1
    no_large_c0 = 2
    no_large_c1 = 2
    no_large_tot = no_large_c0 + no_large_c1
    no_extralarge_c0 = 2 
    no_extralarge_c1 = 2
    no_extralarge_tot = no_extralarge_c0 + no_extralarge_c1
    gini_small = (1 - (((no_small_c0/no_small_tot)**2) + ((no_small_c1/no_small_tot)**2)))
    gini_medium = (1 - (((no_medium_c0/no_medium_tot)**2) + ((no_medium_c1/no_medium_tot)**2)))
    gini_large = (1 - (((no_large_c0/no_large_tot)**2) + ((no_large_c1/no_large_tot)**2)))
    gini_extralarge = (1 - (((no_extralarge_c0/no_extralarge_tot)**2) + ((no_extralarge_c1/no_extralarge_tot)**2)))
    no_shirt_tot = no_small_tot + no_medium_tot + no_large_tot + no_extralarge_tot
    gini_shirt = ((no_small_tot/no_shirt_tot) * gini_small) + ((no_medium_tot/no_shirt_tot) * gini_medium) + ((no_large_tot/no_shirt_tot) * gini_large) + ((no_extralarge_tot/no_shirt_tot) * gini_extralarge)
    print("3e - The gini for shirt size is: " + str(gini_shirt))

    answer["(f) attr for splitting"] = "Car Type"

    # Explanatory text string
    answer["(f) explain choice"] = "Car Type is the best attrbute because it has the least gini index compared to gender and shirt size. The split with ID shouldn't even be considered because it causes overfitting."

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ["binary, quantitative, nominal"]

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = "Time in terms of AM or PM can be discrete or binary, so binary is chosen (AM or PM can be represented by 0 or 1) and binary attributes are considered nominal."

    answer["b"] = ["continuous, quantitative, ratio"]
    answer["b: explain"] = "It is ratio if the light meters have true zero point, otherwise it is an interval."

    answer["c"] = ["discrete, qualitative, ordinal"]
    answer["c: explain"] = "People's judgment can be the light is bright, not so bright, etc which can be categorized but addition or subtraction can't be done."

    answer["d"] = ["continuous, quantitative, ratio"]
    answer["d: explain"] = "Angles can be 29.5 degrees too which is continous and they also have a true zero, so ratio."

    answer["e"] = ["discrete, qualitative, ordinal"]
    answer["e: explain"] = "There are only 3 medals and they can be ordered, so ordinal."

    answer["f"] = ["continuous, quantitative, ratio"]
    answer["f: explain"] = "It is ratio because sea level can be used as a true zero."

    answer["g"] = ["discrete, quantitative, ratio"]
    answer["g: explain"] = "Number of patients in a hospital is countable and also a ratio."

    answer["h"] = ["discrete, qualitative, nominal"]
    answer["h: explain"] = "ISBN numbers are unique and the numbers don't signify any quantitative value and are different to each other (no relation)."

    answer["i"] = ["discrete, qualitative, ordinal"]
    answer["i: explain"] = "The rankings for light can be ordered but they don't measure how much light passes through so it is qualitative"

    answer["j"] = ["discrete, qualitative, ordinal"]
    answer["j: explain"] = "There are only a set number of military ranks and they can be ordered with respect to each other."

    answer["k"] = ["continuous, quantitative, ratio"]
    answer["k: explain"] = "It is a ratio because the true zero can be the center of the campus"

    answer["l"] = ["continuous, quantitative, ratio"]
    answer["l: explain"] = "Density is ratio because we can say a substance is 2 times as dense as another substance because it has zero point."

    answer["m"] = ["discrete, qualitative, nominal"]
    answer["m: explain"] = "Coat check numbers having a value doesn't mean the value signifies anything, the number is just used as a form of ID."

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Though Model 1 has higher accuracy in both training and testing sets which is 0.98 and 0.72, the difference in accuracy between these two sets is large. Which signifies potential overfitting. But Model 2 only had a slight drop in accuracy between training and testing datasets. So Model 2 is better for unseen instances."

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "Still Model 2 is chosen because Model 1 has shown us from the table that it doesn't perform well on unseen data this maybe because it is capturing some noise or other factors (Overfitting can exist too). But Model 2's accuracy difference is far lesser when compared to Model 1's accuracy difference."

    explain["c similarity"] = "Avoid Overfitting"
    explain["c similarity explain"] = "Both MDL and pessimistic error estimate are used to reduce overfitting in a decision tree."

    explain["c difference"] = "Implementation"
    explain["c difference explain"] = "MDL follows occam's razor principle, which is selecting the least complex model. While pessimistic error estimate adds penalty that increases with the number of leaves or splits."

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    #areas of each class
    area_6_a = (0.3 * 0.2) + (0.6 * 0.5) + 0.4
    area_6_b = (0.6 * 0.5) - (0.3 * 0.2)
    area_6_tot = area_6_a + area_6_b
    
    #Gini before split
    gini_before_split = 1 - ((area_6_a**2) + (area_6_b**2))
    

    #The potential splits can be done at x = 0.5, x = 0.2, y = 0.4, y = 0.7

    #gini at x = 0.5 level 1
    split_x1_l_area = 0.5
    split_x1_g_area = 0.5
    area_x1_l_a = (0.5 * 0.4) + (0.2 * 0.3)
    area_x1_l_b = (0.5 * 0.6) - (0.2 * 0.3)
    area_x1_l = area_x1_l_a + area_x1_l_b
    area_x1_g_a = 0.5
    area_x1_g_b = 0
    area_x1_g = area_x1_g_a + area_x1_g_b
    gini_x1_l = (1 - (((area_x1_l_a/area_x1_l) **2) + ((area_x1_l_b/area_x1_l)**2)))
    gini_x1_g = (1 - (((area_x1_g_a/area_x1_g)**2) + ((area_x1_g_b/area_x1_g)**2)))
    gini_x1 = ((split_x1_l_area) * (gini_x1_l)) + ((split_x1_g_area) * (gini_x1_g))
    gini_x1_gain = gini_before_split - gini_x1
    print("6 - The gini for split at x <= 0.5 at level 1 is: "+str(gini_x1))
    print("6 - The gain for split at x <= 0.5 at level 1 is: "+str(gini_x1_gain))

    #gini at x = 0.2 level 1
    split_x2_l_area = 0.2
    split_x2_g_area = 0.8
    area_x2_l_a = (0.2 * 0.4) + (0.2 * 0.3)
    area_x2_l_b = (0.2 * 0.3)
    area_x2_l = area_x2_l_a + area_x2_l_b
    area_x2_g_a = (0.3 * 0.4) + (0.5 * 1.0)
    area_x2_g_b = (0.3 * 0.6)
    area_x2_g = area_x2_g_a + area_x2_g_b
    gini_x2_l = (1 - (((area_x2_l_a/area_x2_l) **2) + ((area_x2_l_b/area_x2_l)**2)))
    gini_x2_g = (1 - (((area_x2_g_a/area_x2_g)**2) + ((area_x2_g_b/area_x2_g)**2)))
    gini_x2 = ((split_x2_l_area) * (gini_x2_l)) + ((split_x2_g_area) * (gini_x2_g))
    gini_x2_gain = gini_before_split - gini_x2
    print("6 - The gini for split at x <= 0.2 at level 1 is: "+str(gini_x2))
    print("6 - The gain for split at x <= 0.2 at level 1 is: "+str(gini_x2_gain))

    #gini at y = 0.4 level 1
    split_y1_l_area = 0.4
    split_y1_g_area = 0.6
    area_y1_l_a = 0.4
    area_y1_l_b = 0
    area_y1_l = area_y1_l_a + area_y1_l_b
    area_y1_g_a = (0.6 * 0.5) + (0.2 * 0.3)
    area_y1_g_b = (0.6 * 0.5) - (0.3 * 0.2)
    area_y1_g = area_y1_g_a + area_y1_g_b
    gini_y1_l = (1 - (((area_y1_l_a/area_y1_l) **2) + ((area_y1_l_b/area_y1_l)**2)))
    gini_y1_g = (1 - (((area_y1_g_a/area_y1_g)**2) + ((area_y1_g_b/area_y1_g)**2)))
    gini_y1 = ((split_y1_l_area) * (gini_y1_l)) + ((split_y1_g_area) * (gini_y1_g))
    gini_y1_gain = gini_before_split - gini_y1
    print("6 - The gini for split at y <= 0.4 at level 1 is: "+str(gini_y1))
    print("6 - The gain for split at y <= 0.4 at level 1 is: "+str(gini_y1_gain))

    #gini at y = 0.7 level 1
    split_y2_l_area = 0.7
    split_y2_g_area = 0.3
    area_y2_l_a = 0.4 + (0.3 * 0.5)
    area_y2_l_b = (0.5 * 0.3)
    area_y2_l = area_y2_l_a + area_y2_l_b
    area_y2_g_a = (0.3 * 0.5) + (0.2 * 0.3)
    area_y2_g_b = (0.3 * 0.3)
    area_y2_g = area_y2_g_a + area_y2_g_b
    gini_y2_l = (1 - (((area_y2_l_a/area_y2_l) **2) + ((area_y2_l_b/area_y2_l)**2)))
    gini_y2_g = (1 - (((area_y2_g_a/area_y2_g)**2) + ((area_y2_g_b/area_y2_g)**2)))
    gini_y2 = ((split_y2_l_area) * (gini_y2_l)) + ((split_y2_g_area) * (gini_y2_g))
    gini_y2_gain = gini_before_split - gini_y2
    print("6 - The gini for split at y <= 0.7 at level 1 is: "+str(gini_y2))
    print("6 - The gain for split at y <= 0.7 at level 1 is: "+str(gini_y2_gain))

    #so we select x<=0.5 for the first split

    #now for 2nd-level, we have the choices of x<=0.2, y<=0.4, y<=0.7
    # first gini of the node
    area_after_split = 0.5
    area_x3_a = (((0.5 * 0.4) + (0.2 * 0.3)) / area_after_split)
    area_x3_b = (((0.5 * 0.6) - (0.2 * 0.3)) / area_after_split)
    gini_after_split = (1 - ((area_x3_a**2) + (area_x3_b**2)))
    
    #gini at x = 0.2 at level 2
    split_x3_l_area = 0.2/0.5
    split_x3_g_area = 0.3/0.5
    area_x3_l_a = (0.2 * 0.4) + (0.2 * 0.3)
    area_x3_l_b = (0.2 * 0.3)
    area_x3_l = area_x3_l_a + area_x3_l_b
    area_x3_g_a = (0.3 * 0.4) 
    area_x3_g_b = (0.3 * 0.6)
    area_x3_g = area_x3_g_a + area_x3_g_b
    gini_x3_l = (1 - (((area_x3_l_a/area_x3_l) **2) + ((area_x3_l_b/area_x3_l)**2)))
    gini_x3_g = (1 - (((area_x3_g_a/area_x3_g)**2) + ((area_x3_g_b/area_x3_g)**2)))
    gini_x3 = ((split_x3_l_area) * (gini_x3_l)) + ((split_x3_g_area) * (gini_x3_g))
    gini_x3_gain = gini_after_split - gini_x3
    print("6 - The gini for split at x <= 0.2 at level 2 is: "+str(gini_x3))
    print("6 - The gain for split at x <= 0.2 at level 2 is: "+str(gini_x3_gain))

    #gini at y = 0.4 at level 2
    split_y3_l_area = 0.2/0.5
    split_y3_g_area = 0.3/0.5
    area_y3_l_a = 0.2
    area_y3_l_b = 0
    area_y3_l = area_y3_l_a + area_y3_l_b
    area_y3_g_a = (0.2 * 0.3)
    area_y3_g_b = (0.6 * 0.5) - (0.3 * 0.2)
    area_y3_g = area_y3_g_a + area_y3_g_b
    gini_y3_l = (1 - (((area_y3_l_a/area_y3_l) **2) + ((area_y3_l_b/area_y3_l)**2)))
    gini_y3_g = (1 - (((area_y3_g_a/area_y3_g)**2) + ((area_y3_g_b/area_y3_g)**2)))
    gini_y3 = ((split_y3_l_area) * (gini_y3_l)) + ((split_y3_g_area) * (gini_y3_g))
    gini_y3_gain = gini_after_split - gini_y3
    print("6 - The gini for split at y <= 0.4 at level 2 is: "+str(gini_y3))
    print("6 - The gain for split at y <= 0.4 at level 2 is: "+str(gini_y3_gain))

    #gini at y = 0.7 at level 2
    split_y4_l_area = 0.35/0.5
    split_y4_g_area = 0.15/0.5
    area_y4_l_a = (0.4 * 0.5)
    area_y4_l_b = (0.3 * 0.5)
    area_y4_l = area_y4_l_a + area_y4_l_b
    area_y4_g_a = (0.2 * 0.3)
    area_y4_g_b = (0.3 * 0.3)
    area_y4_g = area_y4_g_a + area_y4_g_b
    gini_y4_l = (1 - (((area_y4_l_a/area_y4_l) **2) + ((area_y4_l_b/area_y4_l)**2)))
    gini_y4_g = (1 - (((area_y4_g_a/area_y4_g)**2) + ((area_y4_g_b/area_y4_g)**2)))
    gini_y4 = ((split_y4_l_area) * (gini_y4_l)) + ((split_y4_g_area) * (gini_y4_g))
    gini_y4_gain = gini_after_split - gini_y4
    print("6 - The gini for split at y <= 0.7 at level 2 is: "+str(gini_y4))
    print("6 - The gain for split at y <= 0.7 at level 2 is: "+str(gini_y4_gain))

    #so from this we select y <= 0.4 for the level 2 split as it has the most gain

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = "x <= 0.5"
    answer["a, level 2, right"] ="A"
    answer["a, level 2, left"] = "y <= 0.4"
    answer["a, level 3, left"] = "A"
    answer["a, level 3, right"] = "B"

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    misclassified_area = 0.2 * 0.3
    total_area_6 = 1.0
    expected_error = misclassified_area/total_area_6
    print("6 - The expected error rate is: "+str(expected_error))
    answer["b, expected error"] = 0.06 # Around 6%

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("x <= 0.5")
    x_lesser_left = tree.insert_left("y <= 0.4") 
    tree.insert_right("A")
    x_lesser_left.insert_left("A")
    x_lesser_left.insert_right("B")
    

    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.5310044064107188

    # 7 - part a
    # calculating initial entropy
    positive_examples_i = 10
    negative_examples_i = 10
    total_examples_i = positive_examples_i + negative_examples_i
    entropy_before = (-((positive_examples_i/total_examples_i) * u.log2 (positive_examples_i/total_examples_i)) - ((negative_examples_i/total_examples_i) * u.log2 (negative_examples_i/total_examples_i)))
    print ("7a - Total entropy before split: " + str(entropy_before))

    #The entropy for splitting by ID would be 0 in every case because every node will be pure (As ID is different and unique for every person)
    information_gain_7a = entropy_before - 0
    print("7a - The information gain using ID attribute: " + str(information_gain_7a))

    # 7 - part b
    # calculating handedness entropy (Split into left or right handend)
    # First the split for left-handedness
    positive_examples_l = 9
    negative_examples_l = 1
    total_examples_l = positive_examples_l + negative_examples_l
    entropy_left = (-((positive_examples_l/total_examples_l) * u.log2 (positive_examples_l/total_examples_l)) - ((negative_examples_l/total_examples_l) * u.log2 (negative_examples_l/total_examples_l)))
    print ("7b - Entropy for left-handed split: " + str(entropy_left))

    # The split for right-handedness 
    positive_examples_r = 1
    negative_examples_r = 9
    total_examples_r = positive_examples_r + negative_examples_r
    entropy_right = (-((positive_examples_r/total_examples_r) * u.log2 (positive_examples_r/total_examples_r)) - ((negative_examples_r/total_examples_r) * u.log2 (negative_examples_r/total_examples_r)))
    print ("7b - Entropy for right-handed split: " + str(entropy_right))

    # Now we calculate information gain for part b
    split_left = 10
    split_right = 10
    split_total = split_left + split_right
    information_gain_7b = (entropy_before - (((split_left/split_total) * (entropy_left)) + ((split_right/split_total) * (entropy_right))))
    print("7b - The information gain with handedness split is: " + str(information_gain_7b))

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"
    # ID will be chosen becuase it has more information gain, but this shouldn't be the case as this will lead to overfitting.

    # answer is a float
    answer["d, gain ratio, ID"] = 0.23137821315975915
    answer["e, gain ratio, Handedness"] = 0.5310044064107188

    # 7 - part d
    split_id = 1
    split_info_id = (-20 * ((split_id/split_total) * u.log2(split_id/split_total)))
    # here multiplying by 20 because there are 20 splits and each split has 1 element 
    print("7d - The split info for ID split is: " + str(split_info_id))
    gain_ratio_id = (information_gain_7a/split_info_id)
    print("7d - The gain ratio for ID split is: " + str(gain_ratio_id))

    # 7 - part e
    split_info_handedness = -(((split_left/split_total) * u.log2(split_left/split_total)) + ((split_right/split_total) * u.log2(split_right/split_total)))
    print("7e - The split info for handedness split is: " + str(split_info_handedness))
    gain_ratio_handedness = (information_gain_7b/split_info_handedness)
    print("7e - The gain ratio for handedness split is: " + str(gain_ratio_handedness))
    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"
    # Because handedness has larger gain ratio when compared to the split with ID

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

