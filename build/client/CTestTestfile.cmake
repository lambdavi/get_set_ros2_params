# CMake generated Testfile for 
# Source directory: /home/dave/team/test_ws/src/client
# Build directory: /home/dave/team/test_ws/build/client
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(copyright "/usr/bin/python3" "-u" "/opt/ros/dashing/share/ament_cmake_test/cmake/run_test.py" "/home/dave/team/test_ws/build/client/test_results/client/copyright.xunit.xml" "--package-name" "client" "--output-file" "/home/dave/team/test_ws/build/client/ament_copyright/copyright.txt" "--command" "/opt/ros/dashing/bin/ament_copyright" "--xunit-file" "/home/dave/team/test_ws/build/client/test_results/client/copyright.xunit.xml")
set_tests_properties(copyright PROPERTIES  LABELS "copyright;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/dave/team/test_ws/src/client")
add_test(flake8 "/usr/bin/python3" "-u" "/opt/ros/dashing/share/ament_cmake_test/cmake/run_test.py" "/home/dave/team/test_ws/build/client/test_results/client/flake8.xunit.xml" "--package-name" "client" "--output-file" "/home/dave/team/test_ws/build/client/ament_flake8/flake8.txt" "--command" "/opt/ros/dashing/bin/ament_flake8" "--xunit-file" "/home/dave/team/test_ws/build/client/test_results/client/flake8.xunit.xml")
set_tests_properties(flake8 PROPERTIES  LABELS "flake8;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/dave/team/test_ws/src/client")
add_test(lint_cmake "/usr/bin/python3" "-u" "/opt/ros/dashing/share/ament_cmake_test/cmake/run_test.py" "/home/dave/team/test_ws/build/client/test_results/client/lint_cmake.xunit.xml" "--package-name" "client" "--output-file" "/home/dave/team/test_ws/build/client/ament_lint_cmake/lint_cmake.txt" "--command" "/opt/ros/dashing/bin/ament_lint_cmake" "--xunit-file" "/home/dave/team/test_ws/build/client/test_results/client/lint_cmake.xunit.xml")
set_tests_properties(lint_cmake PROPERTIES  LABELS "lint_cmake;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/dave/team/test_ws/src/client")
add_test(pep257 "/usr/bin/python3" "-u" "/opt/ros/dashing/share/ament_cmake_test/cmake/run_test.py" "/home/dave/team/test_ws/build/client/test_results/client/pep257.xunit.xml" "--package-name" "client" "--output-file" "/home/dave/team/test_ws/build/client/ament_pep257/pep257.txt" "--command" "/opt/ros/dashing/bin/ament_pep257" "--xunit-file" "/home/dave/team/test_ws/build/client/test_results/client/pep257.xunit.xml")
set_tests_properties(pep257 PROPERTIES  LABELS "pep257;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/dave/team/test_ws/src/client")
add_test(xmllint "/usr/bin/python3" "-u" "/opt/ros/dashing/share/ament_cmake_test/cmake/run_test.py" "/home/dave/team/test_ws/build/client/test_results/client/xmllint.xunit.xml" "--package-name" "client" "--output-file" "/home/dave/team/test_ws/build/client/ament_xmllint/xmllint.txt" "--command" "/opt/ros/dashing/bin/ament_xmllint" "--xunit-file" "/home/dave/team/test_ws/build/client/test_results/client/xmllint.xunit.xml")
set_tests_properties(xmllint PROPERTIES  LABELS "xmllint;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/dave/team/test_ws/src/client")
