#FNA#
while { 1==1 } {
*createmarkpanel elements 1 "Please Select the Element:"
set main_element [hm_getmark elements 1]
*clearmark elements 1
if {$main_element == ""} {
break
}
*createmarkpanel nodes 1 "Please Select the Corner Node:"
set corner_node [hm_getmark nodes 1]
*clearmark nodes 1
*currentcollector components [hm_getvalue components id=[hm_getvalue elems id=$main_element dataname=collector] dataname=name]
set node_list [hm_nodelist $main_element]
set node1 [lindex $node_list 0]
set node2 [lindex $node_list 1]
set node3 [lindex $node_list 2]
set node4 [lindex $node_list 3]
set center_x [lindex [hm_entityinfo centroid elems $main_element] 0]
set center_y [lindex [hm_entityinfo centroid elems $main_element] 1]
set center_z [lindex [hm_entityinfo centroid elems $main_element] 2]
*createnode $center_x $center_y $center_z 0 0 0
*createmark nodes 1 -1
set center_id [hm_getmark nodes 1]
*clearmark nodes 1
set neighbour_1 [lindex $node_list [expr ([lsearch -exact $node_list $corner_node] + 1) %4 ]]
set neighbour_2 [lindex $node_list [expr ([lsearch -exact $node_list $corner_node] - 1) %4 ]]
foreach temp $node_list {
if {[lsearch -exact [list $corner_node $neighbour_1 $neighbour_2] $temp] == -1} {
set other_corner $temp
}
}
set mid_1_x [expr ([hm_getvalue nodes id=$neighbour_1 dataname=globalx] + [hm_getvalue nodes id=$corner_node dataname=globalx]) / 2]
set mid_1_y [expr ([hm_getvalue nodes id=$neighbour_1 dataname=globaly] + [hm_getvalue nodes id=$corner_node dataname=globaly]) / 2]
set mid_1_z [expr ([hm_getvalue nodes id=$neighbour_1 dataname=globalz] + [hm_getvalue nodes id=$corner_node dataname=globalz]) / 2]
set mid_2_x [expr ([hm_getvalue nodes id=$neighbour_2 dataname=globalx] + [hm_getvalue nodes id=$corner_node dataname=globalx]) / 2]
set mid_2_y [expr ([hm_getvalue nodes id=$neighbour_2 dataname=globaly] + [hm_getvalue nodes id=$corner_node dataname=globaly]) / 2]
set mid_2_z [expr ([hm_getvalue nodes id=$neighbour_2 dataname=globalz] + [hm_getvalue nodes id=$corner_node dataname=globalz]) / 2]
*createnode $mid_1_x $mid_1_y $mid_1_z 0 0 0
*createmark nodes 1 -1
set mid_1_id [hm_getmark nodes 1]
*clearmark nodes 1
*createnode $mid_2_x $mid_2_y $mid_2_z 0 0 0
*createmark nodes 1 -1
set mid_2_id [hm_getmark nodes 1]
*clearmark nodes 1
*elementtype 104 1
*createlist nodes 1 $corner_node $mid_1_id $center_id $mid_2_id
*createelement 104 1 1 1
*createlist nodes 1 $mid_1_id $neighbour_1 $other_corner $center_id
*createelement 104 1 1 1
*createlist nodes 1 $center_id $other_corner $neighbour_2 $mid_2_id
*createelement 104 1 1 1
*createmark nodes 1 $center_id $mid_1_id $mid_2_id
*nodemarkcleartempmark 1
*createmark elements 1 $main_element
*deletemark elements 1
puts "MISSION ACCOMPLISHED."
}