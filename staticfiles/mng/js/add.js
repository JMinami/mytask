
$(function(){
    //レベル選択ボタンクリック
    $('.dropdown-item').click(function(){
        var text = $(this).val();
        var number = Number(text)
        $('#level').val(number);
    });

    //入力値チェック
    $('#submit-button').click(function(){
        /* タスク名判定 */
        var name = $('#name').val();
        var level = $('#level').val();
        var overall = $('#overall').val();
        if(name===''||level===''||overall===''){
            alert('入力されていない項目があります');
            return false;
        }
        return true;
    });
});

function submitClick(){
    alert('test');
}
