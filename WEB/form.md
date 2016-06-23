# Guidelines
1. For every form field, ensure that a descriptive label is provided and use the <label> element to identify each form control.
每個form表單欄位都要有label標籤註明用途。

> When these labels are marked up correctly, people can interact with them using only the keyboard, using voice input, and using screen readers. Also, the label itself becomes clickable, which enables a person who has difficulty clicking on small radio buttons or checkboxes to click anywhere on the label text.

> Whenever possible, use the label element to explicitly associate text with form elements. The for attribute of the label must exactly match the id of the form control.

example:
```html
<label for="firstname">First name:</label>
<input type="text" name="firstname" id="firstname"><br>
```
確認label的 for 與 關聯元件的name相符合
the label will become clickable
2. For larger or complex forms, use the ``<fieldset>`` and ``<legend>`` elements to respectively group and associate related form controls.

較複雜的form表單需用``<fieldset>``跟``<legend>``元件來分類與聯繫表單控件。

``` Grouping needs to be carried out visually and in the code, for example, by using the <fieldset> and <legend> elements to associate related form controls. The <fieldset> identifies the entire grouping and <legend> identifies the grouping's descriptive text.
```

## ref
[Edx HTML5.1x HTML5 Part 1: HTML5 Coding Essentials and Best Practices](https://courses.edx.org/courses/course-v1:W3Cx+HTML5.1x+2T2016/courseware/36a27299952f4ecf87066b10a1928bb5/44531be3beee456bb3c0a2c8b03e9aeb/)

[accessibility](https://www.w3.org/WAI/tutorials/forms/)
[how to construct form](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms/How_to_structure_an_HTML_form)
