$(function(){
    $('#datetimepicker').datepicker({dateFormat:'yy-mm-dd'});

    //追加ボタンクリック
    $('#submit-button').click(function(){
        /* 入力されていない項目があるかチェック */
        var date = $('#datetimepicker').val();
        var progress = $('#progress').val();

        if(isNaN(progress))
        {
            alert('進捗には数値を入力してください')
            return false;
        }
        if(date===''||progress==='')
        {
            alert('進捗と日付は必ず入力してください');
            return false;
        }
        /* レベルを超えていないかチェック */
        var level = Number($('#level').text());
        var current_level = Number($('#current_level').text());
        var sum = current_level + Number(progress);

        if(level < sum)
        {
            alert('進捗がレベルを超えています');
            return false;
        }


    });
});